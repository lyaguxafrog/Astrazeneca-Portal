# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from urllib.parse import urlparse

def validate_relative_or_absolute_url(value: str) -> None:
    """
    Сервис проверки ссылки

    :param value: Ссылка

    :return: None
    """
    url_validator = URLValidator()

    # Проверяем, является ли введенное значение полным URL
    try:
        url_validator(value)
    except ValidationError:
        # Если не является полным URL, проверяем, является ли относительным URL
        if not value.startswith('/'):
            raise ValidationError('Введите действительный URL или относительный URL.')
