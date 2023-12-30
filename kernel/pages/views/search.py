from django.db.models import Q, Value, CharField
from rest_framework import generics
from rest_framework.response import Response
from pages.models import Articles, ContentBlock, Drug, DrugFAQ, Events, VideoLectures
from pages.serializers import SearchSerializer


class SearchAPIView(generics.ListAPIView):
    serializer_class = SearchSerializer

    def get_queryset(self):
        search_param = self.kwargs.get('query')

        articles_queryset = Articles.objects.filter(
            Q(article_name__icontains=search_param) |
            Q(short_description__icontains=search_param) |
            Q(final_content__icontains=search_param) |
            Q(access_number__icontains=search_param)
        ).annotate(model_type=Value('article', output_field=CharField()))

        content_blocks_queryset = ContentBlock.objects.filter(
            Q(text__icontains=search_param)
        ).annotate(model_type=Value('content_block', output_field=CharField()))

        drugs_queryset = Drug.objects.filter(
            Q(name__icontains=search_param) |
            Q(brief_info__icontains=search_param) |
            Q(approvals_and_decodings__icontains=search_param)
        ).annotate(model_type=Value('drug', output_field=CharField()))

        drug_faqs_queryset = DrugFAQ.objects.filter(
            Q(title__icontains=search_param) |
            Q(text__icontains=search_param)
        ).annotate(model_type=Value('drug_faq', output_field=CharField()))

        events_queryset = Events.objects.filter(
            Q(name__icontains=search_param) |
            Q(text__icontains=search_param)
        ).annotate(model_type=Value('event', output_field=CharField()))

        video_lectures_queryset = VideoLectures.objects.filter(
            Q(video_article__icontains=search_param) |
            Q(short_description__icontains=search_param) |
            Q(conspect__icontains=search_param) |
            Q(access_number__icontains=search_param)
        ).annotate(model_type=Value('video_lecture', output_field=CharField()))

        queryset = (
            list(articles_queryset.values('id', 'article_name', 'model_type', model=Value('article'))) +
            list(content_blocks_queryset.values('id', 'text', 'model_type', model=Value('content_block'))) +
            list(drugs_queryset.values('id', 'name', 'model_type', model=Value('drug'))) +
            list(drug_faqs_queryset.values('id', 'title', 'model_type', model=Value('drug_faq'))) +
            list(events_queryset.values('id', 'name', 'model_type', model=Value('event'))) +
            list(video_lectures_queryset.values('id', 'video_article', 'model_type', model=Value('video_lecture')))
        )

        return queryset
