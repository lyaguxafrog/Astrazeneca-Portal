# -*- coding: utf-8 -*-


from django.core.exceptions import ValidationError
from six import PY3
import imghdr

from django.core.exceptions import ValidationError
from six import PY3
import imghdr

def validate_svg(value):
    """
    Сервис проверки файла на SVG
    """
    if value:
        if hasattr(value.file, 'content_type'):
            content_type = value.file.content_type
        else:
            content_type = imghdr.what(value)

        if content_type != 'image/svg+xml':
            raise ValidationError('Not a valid SVG file.', code='invalid')


def validate_max_4_files(value):
    """
    Сервис проверки кол-ва файлов
    """
    if value and len(value) > 4:
        raise ValidationError(_('No more than 4 files are allowed.'),
                              code='invalid')
