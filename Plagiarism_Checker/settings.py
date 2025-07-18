from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------- SECURITY -----------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'jjhy1%zxbzl@z$oqh75zm+e(%-d7r-biy!2=_v1h^@zsn08=-8')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Robust ALLOWED_HOSTS parsing for env variables, default for local dev
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,django-plagiarism-checker.onrender.com').split(',')
    if host.strip()
]

# ----------------- APPLICATION ----------------------
INSTALLED_APPS = [
    'plagiarismchecker.apps.PlagiarismcheckerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add other required apps below
    # e.g., 'rest_framework', 'crispy_forms', etc.
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files in production
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
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600,
        ssl_require=False  # Set True only if required
    )
}

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
# In Render dashboard set:
# - SECRET_KEY=your-secret-key
# - DEBUG=False
# - ALLOWED_HOSTS=django-plagiarism-checker.onrender.com
#
# After each deploy:
# - python manage.py migrate
# - python manage.py createsuperuser
# - python manage.py collectstatic --noinput

# ------------------- EXTRA (Optional) ----------------
# import django_heroku
# django_heroku.settings(locals())
