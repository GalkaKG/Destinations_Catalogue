from pathlib import Path
from django.urls import reverse_lazy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', 1)))  # Now is True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ')
CSRF_TRUSTED_ORIGINS = [f'http://{x}:80' for x in os.environ.get('ALLOWED_HOSTS', '').split(' ')]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'Destinations_Catalogue.common',
    'Destinations_Catalogue.destinations',
    'Destinations_Catalogue.profiles',
    'Destinations_Catalogue.explore',

    # Third party apps
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'Destinations_Catalogue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Destinations_Catalogue.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME', None),
        "USER": os.getenv('DB_USER', None),
        "PASSWORD": os.getenv('DB_PASSWORD', None),
        "HOST": os.getenv('DB_HOST', None),
        "PORT": os.getenv('DB_PORT', '5432'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATIC_ROOT = BASE_DIR / 'static_root'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'

# MEDIA_ROOT = (
#         BASE_DIR / 'media_root/'
# )
MEDIA_ROOT = (
        BASE_DIR / 'media/'
)


AUTH_USER_MODEL = 'profiles.CustomUser'

LOGIN_REDIRECT_URL = reverse_lazy('create profile')

LOGIN_URL = reverse_lazy('login')


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
