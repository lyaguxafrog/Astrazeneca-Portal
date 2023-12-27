from rest_framework import generics
from django.db.models import Q
from pages.models import (Articles, ContentBlock, Drug, Icon, Events, VideoLectures)
from pages.serializers import (SearchArticleSerializer, SearchContentBlockSerializer, SearchDrugSerializer, SearchEventsSerializer, SearchVideoLecturesSerializer)
from django.db.models import CharField


class SearchAPIView(generics.ListAPIView):
    # Replace the following line with your default queryset
    queryset = Drug.objects.none()
    serializer_class_dict = {
        Articles: SearchArticleSerializer,
        ContentBlock: SearchContentBlockSerializer,
        Drug: SearchDrugSerializer,
        Events: SearchEventsSerializer,
        VideoLectures: SearchVideoLecturesSerializer
    }

    def get_queryset(self):
        query = self.kwargs['query']

        # Define a common set of fields for all models
        common_fields = ['text', 'description']  # Add more fields as needed

        # Define the fields you want to search across for each model
        search_fields_dict = {
            Articles: common_fields + ['article_name'],
            ContentBlock: common_fields + ['article', 'text'],
            Drug: common_fields + ['name', 'brief_info', 'instruction_text'],
            Events: common_fields + ['name', 'date', 'text'],
            VideoLectures: common_fields + ['video_article', 'short_description', 'conspect']
        }

        # Initialize an empty queryset
        combined_queryset = Drug.objects.none()

        # Iterate through each model and perform a separate query
        for model, search_fields in search_fields_dict.items():
            model_query = Q()
            for field in search_fields:
                lookup = f'{field}__icontains' if isinstance(model._meta.get_field(field), CharField) else field
                model_query |= Q(**{lookup: query})
            queryset = model.objects.filter(model_query)
            combined_queryset = combined_queryset.union(queryset)

        return combined_queryset

    def get_serializer_class(self):
        # Determine the appropriate serializer based on the model in the queryset
        model = self.queryset.model
        return self.serializer_class_dict.get(model)
