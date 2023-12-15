# -*- coding: utf-8 -*-


from django.urls import path, include

urlpatterns = [
    path('specialties/', include('pages.all_urls.specialty_urls')),
    path('stories/', include('pages.all_urls.story_urls')),
\
]
