# Django settings for djangology project.
import sys
import os
sys.path.append(os.getcwd())

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('yu', 'liangyu.teq@gmail.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = 'djangology'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'root'             # Not used with sqlite3.
#DATABASE_PASSWORD = '240908teq'         # Not used with sqlite3.
#DATABASE_HOST = '/tmp/mysql.sock'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'
#MEDIA_URL = 'file:///Users/ema/code/djangology/dj/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/amedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yl' ## Yu add 09/29/2015






# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
                    # 'django.template.loaders.filesystem.load_template_source',
                    #Yu modified 09/29/15
 'django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader',
                    ######
                    #'django.template.loaders.app_directories.load_template_source',
#  'django.template.loaders.eggs.load_template_source',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
                      ## Yu add 09/29/15
     #'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'djangology.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.getcwd(), '/dj/templates'),
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
	'django.contrib.markup',
    'import_export',
                  
	'dj',
                # YU 09/16
                  #'reporting',
]
##Yu Modify 09/29/15
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
         'NAME': 'djangology',
         'USER': 'root',
         'PASSWORD' : '240908teq',
         'HOST': '',
         'PORT': '',
                }
}


LOGIN_REDIRECT_URL='/documents'
