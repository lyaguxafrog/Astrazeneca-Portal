# -*- coding: utf-*- -*-

from django.http import JsonResponse

from decouple import config



def login_link(request):
    source = config('OUR_DOMAIN')
    next_url = config('OUR_DOMAIN')

    login_url = f"https://sso.az.clients.dobroagency.ru/signup?source={source}&next_url={next_url}"

    return JsonResponse({"login_link": login_url})
