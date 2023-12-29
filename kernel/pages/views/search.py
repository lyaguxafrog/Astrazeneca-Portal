# -*- coding: utf-8 -*-

from django.shortcuts import render
from haystack.query import SearchQuerySet

def search(request):
    query = request.GET.get('q', '')
    results = SearchQuerySet().filter(content=query)

    return render(request,
            'search_results.html', {'results': results, 'query': query})
