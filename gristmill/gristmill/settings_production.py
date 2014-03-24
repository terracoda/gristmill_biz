# Django settings for gristmill project.
#import os.path

# 1.check - DEBUGging off
DEBUG = False
# 2.check - TEMPLATE_DEBUGging off (set to FALSE)
TEMPLATE_DEBUG = False

# 3. check - ADMIN emails set
# 4. Make sure EMAIL_HOST setting is set to the proper hostname for your mail server. Might also need to set EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT or EMAIL_USE_TLS. EMAIL_SUBJECT_PREFIX is [Django] by default.
ADMINS = (
     ('Tali Smith', 'terracoda@gmail.com'), 
     ('Tali Smith', 'tali@gristmill.webfactional.com'),
)
# 5. Broken links
SEND_BROKEN_LINK_EMAILS = TRUE
MANAGERS = ( 
     ('Tali Smith', 'tali@gristmill.webfactional.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', or 'sqlite3'.
        'NAME': 'gristmill_db', # Or path to database file if using sqlite3.
        'USER': 'gristmill',                      # Not used with sqlite3.
        'PASSWORD': 'kitty2!',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/St_Johns'
#TIME_ZONE = 'Canada/Newfoundland'
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/gristmill/webapps/gristmill_dj/gristmill/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/gristmill/webapps/gristmill_dj/gristmill/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://gristmill.webfactional.com/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	"/home/gristmill/webapps/gristmill_dj/gristmill/static/",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y5%d3$@=y)xek0@z&amp;l(yf@9j&amp;@uy=djlkg1&amp;j1ptw4w_&amp;ibboh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'flatpages_plus.middleware.FlatpageFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gristmill.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'gristmill.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
   '/home/gristmill/webapps/gristmill_dj/gristmill/templates', # Change this to your own directory.
   '/home/gristmill/webapps/gristmill_dj/gristmill/my_tags/templatetags/templates', # Change this to your own directory.
)
#TEMPLATE_DIRS = (	 
#    os.path.join(os.path.dirname(__file__), 'templates'),
#)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request', # needed for django-menu
    ## Using template tags instead of context processors
    #'testimonials.context_processors.get_testimonial',
    #'daily_grist.context_processors.get_recent_entries',
    #'galleria.context_processors.get_recent_images',
    #'homepage.context_processors.get_page_intros',
    )

INSTALLED_APPS = (
    'django.contrib.auth',
#    'django.contrib.comments'
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    ## Below are apps from the community
#    'autoslug'    
#    'flatpages_plus',
    'menu', #<http://www.rossp.org>
    'taggit',
    ## tinymce stuff
#    'flatpages_tinymce'
#    'tinymce',
    ## My apps
    'contact',
    'daily_grist',
    'galleria',
    'homepage',    
    'my_tags',  
    'testimonials', 
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
