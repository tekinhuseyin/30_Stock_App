pip install django-cors-headers

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
  # ...
  'corsheaders',
]


MIDDLEWARE = [
  # ...
  'django.contrib.sessions.middleware.SessionMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  # ...
]

# add settings.py
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = (
  'Access-Control-Allow-Origin: *',
)
