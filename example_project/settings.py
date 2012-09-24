import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__)))
SECRET_KEY = 'k^+o!9jb-6hc*9dlrm$x!#2^zpond1u9=sob4p4(s-@v8(0(q('
TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)
MIDDLEWARE_CLASSES = ('django.middleware.common.CommonMiddleware',
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',)
ROOT_URLCONF = 'example_project.urls'
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'glossary',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'example_project/glossary.db',
    },
}

try:
    from local_settings import *
except ImportError:
    pass
