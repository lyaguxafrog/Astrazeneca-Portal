from pathlib import Path
from decouple import config
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = (os.getenv('DEBUG_FLAG') == 'True')
DOCS = (os.getenv('DOCS_FLAG') == 'True')

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [os.getenv("OUR_DOMAIN"),
                     f'{os.getenv("OUR_DOMAIN")}:8000',
                     f'https://{os.getenv("OUR_DOMAIN")}']


    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    #FIXME: исправить что тут происходит
    # CSRF_COOKIE_DOMAIN = f'https://{os.getenv("OUR_DOMAIN")}'
    CSRF_TRUSTED_ORIGINS = [f'https://{os.getenv("OUR_DOMAIN")}']



INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'ckeditor',
    'multiupload',
    'haystack',
    'drf_haystack',
    'django_cleanup.apps.CleanupConfig',
    'django_unused_media',
    'adminsortable2',
    'nested_admin',
    'polymorphic',

    'pages',
    'users',
    'practics',
]

CKEDITOR_CONFIGS = {
    'default': {
        'height': 300,
        'width': 650,
        'toolbar': [
            ['Format', 'Heading', 'FontSize', 'Font', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['NumberedList', 'BulletedList'],
            ['TextColor', 'Table'],
            ['Link', 'Unlink'],
            ['Image', 'Source'],
        ],
        'language': 'ru',
        'extraPlugins': ','.join(['font', 'colorbutton']),
        'font_names': 'Arial;Comic Sans MS;Courier New;Georgia;Times New Roman;Verdana',
        'fontSize_sizes': '8/8px;10/10px;12/12px;14/14px;16/16px;18/18px;24/24px;36/36px',
        'colorButton_colors': 'e50914,3f3f3f,00bcd4,2196f3,4caf50,ffeb3b,ff9800,ff5722',
        'startupFocus': 'Ваш собственный текст здесь.',
        'ImageAltRequired': False,
    },
}



HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "pages.services.range_response.RangeHeaderMiddleware"
]

ROOT_URLCONF = "config.urls"


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://astraportal.dev-demo.online",
    "https://astraportal.dev-demo.online",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [
            os.path.join(BASE_DIR, "frontend/dist"),
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                'django.template.context_processors.request',
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': "db",
        'PORT': 5432,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_URLS_REGEX = r'^/swagger(?P<url>.*)$'
