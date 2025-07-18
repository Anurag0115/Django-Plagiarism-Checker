from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------- SECURITY -----------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'jjhy1%zxbzl@z$oqh75zm+e(%-d7r-biy!2=_v1h^@zsn08=-8')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# ----------------- APPLICATION ----------------------
INSTALLED_APPS = [
    'plagiarismchecker.apps.PlagiarismcheckerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Plagiarism_Checker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Plagiarism_Checker.wsgi.application'

# ------------------- DATABASES ----------------------
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600
    )
}
# In production, set the 'DATABASE_URL' env variable (Render/Heroku does this for you).

# ------------------- PASSWORD VALIDATORS -------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------ INTERNATIONALIZATION -------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ------------------- STATIC & MEDIA ------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# ------------------- DEPLOYMENT NOTES ----------------
# When deploying, make sure to set SECRET_KEY, DEBUG=False, and ALLOWED_HOSTS in your platform's dashboard.
# Run: python manage.py collectstatic
# Gunicorn/WSGI will serve from STATIC_ROOT using Whitenoise middleware.
# For local dev, SQLite will be used. Cloud platforms inject DATABASE_URL for Postgres.

# ------------------- HEROKU (OPTIONAL) ---------------
# import django_heroku
# django_heroku.settings(locals())
