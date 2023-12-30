from itertools import chain

from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from pages.models import Articles, VideoLectures, Drug, Events


class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        q = request.GET.get('q')
        if q:
            query_sets = []  # Total QuerySet

            # Searching for all models
            query_sets.append(Articles.objects.search(query=q))
            query_sets.append(VideoLectures.objects.search(query=q))
            query_sets.append(Drug.objects.search(query=q))
            query_sets.append(Events.objects.search(query=q))

            # and combine results
            final_set = list(chain(*query_sets))
            final_set.sort(key=lambda x: x.pub_date, reverse=True)  # Sorting

            context['last_question'] = '?q=%s' % q

            current_page = Paginator(final_set, 10)

            page = request.GET.get('page')
            try:
                context['object_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['object_list'] = current_page.page(1)
            except EmptyPage:
                context['object_list'] = current_page.page(current_page.num_pages)

        return render(request=request, template_name=self.template_name, context=context)
