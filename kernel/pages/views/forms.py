# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from pages.models import Articles
from pages.services.forms import ArticlesForm

def create_article(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            # Дополнительные действия при сохранении статьи
    else:
        form = ArticlesForm()

    return render(request, 'static/form_tamplate.html', {'form': form})
