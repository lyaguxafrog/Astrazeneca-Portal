# -*- coding: utf-*- -*-

from django.http import JsonResponse
from django.shortcuts import reverse

from decouple import config


def registration_link(request):
    source = config('OUR_DOMAIN')
    next_url = reverse(config('REDIRECT_URL'))
    registration_url = f"sso.azmost.ru/signup?source={source}&next_url={next_url}"

    return JsonResponse({"registration_link": registration_url})



def login_link(request):
    source = config('OUR_DOMAIN')
    next_url = reverse(config('REDIRECT_URL'))

    login_url = f"sso.azmost.ru/signin?source={source}&next_url={next_url}"

    return JsonResponse({"login_link": login_url})
