# -*- coding: utf-8 -*-


class CustomHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Добавьте нужные вам заголовки
        response["X-Custom-Header"] = "Custom Value"
        response["Another-Header"] = "Another Value"

        return response
