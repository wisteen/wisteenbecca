
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v6#2399_3(1vs_tcdg!1*f)y19tq7e&_=050aqdz$p^(b%o)^!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CSRF_TRUSTED_ORIGINS = [
    'https://wisteenbecca.onrender.com',
    # You can add other domains if needed
]




ALLOWED_HOSTS = ["localhost", "0.0.0.0", "wisteenbecca.onrender.com","*", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # create other apps
    'proposal',
    'shareafric_app',
    'ckeditor',
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

ROOT_URLCONF = 'config.urls'

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

# WSGI_APPLICATION = 'config.wsgi.application'

ASGI_APPLICATION = 'config.asgi.application'
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# Database connection configuration for PostgreSQL on Render
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://wisteen:nbhznd0UDdWd7J7JT4ZsjkO0uziOuRJD@dpg-cte93k5umphs73bb3lh0-a.oregon-postgres.render.com/message_iixu'
    )
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
# Directory where static files will be collected for production (absolute path)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional directories where Django will look for static files (e.g., app-specific static directories)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_rabbitmq.core.RabbitmqChannelLayer",
#         "CONFIG": {
#             "host":"amqp://guest:guest@127.0.0.1:5672/",
#         },
#     },
# }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

WHATSAPP_URL="https://graph.facebook.com/v21.0/484038361468119/messages"
WHATSAPP_TOKEN="Bearer EAARS1iKIw8MBOzayUZBOPeVZAKMHfdOeu2mXPCChLBkdXCje9uEfeZAdUjZAedOiHRbGSzfUY7870Od2UL32EXZAzSScuxXw2Lk6K2biZAiEdqi2FMzLWmy6bFoLKHWRZBmRCs98pqpZCP7i5nW0lZBetrtOSJMyuDo4Ym6UmVffNyZBbvVnlZBeotDZCKdTzDQZAgod8g8nArgZCYyn6LZACLfm5tgB1CWkC2wZBFnYg7rEw9ScXCsg"



JAZZMIN_SETTINGS = {
    # Title of the window
    "site_title": "Rebecca Douglas Portfolio",

    # Title on the login screen
    "site_header": "Rebecca's Dashboard",

    # Title on the brand
    "site_brand": "Rebecca Douglas",

    # Logo for the site
    "site_logo": "assets/img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Rebecca Douglas' Portfolio",

    # Copyright on the footer
    "copyright": "© 2024 Rebecca Douglas",

    # List of model admins to search from the search bar
    "search_model": ["portfolio.Project", "portfolio.Client"],

    # User avatar field
    "user_avatar": "assets/img/hero-bg.jpg",

    ############
    # Top Menu #
    ############

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Portfolio", "url": "portfolio:project_list", "permissions": ["portfolio.view_project"]},
        {"name": "Contact", "url": "https://rebeccadouglas.com/contact", "new_window": True},
        {"model": "portfolio.Client"},
    ],

    #############
    # User Menu #
    #############

    "usermenu_links": [
        {"name": "My Profile", "url": "admin:auth_user_change", "new_window": False},
        {"name": "Support", "url": "https://support.rebeccadouglas.com", "new_window": True},
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to auto-expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating the side menu
    "hide_apps": [],

    # Custom links to append to app groups
    "custom_links": {
        "portfolio": [
            {
                "name": "Add Project",
                "url": "admin:portfolio_project_add",
                "icon": "fas fa-plus-circle",
                "permissions": ["portfolio.add_project"]
            },
            {
                "name": "View Reports",
                "url": "portfolio:reports",
                "icon": "fas fa-chart-line",
                "permissions": ["portfolio.view_reports"]
            },
        ]
    },

    # Custom icons for side menu apps/models
    "icons": {
        "auth": "fas fa-users-cog",
        "portfolio.Project": "fas fa-folder-open",
        "shareafric_app.Client": "fas fa-user-tie",
        "shareafric_app.Client": "fas fa-user-tie",
        "shareafric_app.Service": "fas fa-concierge-bell",  # Service
        "shareafric_app.SkillRight": "fas fa-tasks",       # SkillRight
        "shareafric_app.SkillLeft": "fas fa-tasks",        # SkillLeft
        "shareafric_app.Summary": "fas fa-id-card",        # Summary
        "shareafric_app.Education": "fas fa-graduation-cap", # Education
        "shareafric_app.Experience": "fas fa-briefcase",   # Experience
        "shareafric_app.ContactUs": "fas fa-envelope",     # ContactUs
        "shareafric_app.Facts": "fas fa-chart-bar",        # Facts
        "shareafric_app.Portfolio": "fas fa-th-large",     # Portfolio
    },
    # Default icons
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-file",

    #################
    # Related Modal #
    #################

    "related_modal_active": True,

    #############
    # UI Tweaks #
    #############

    "custom_css": "portfolio/css/custom.css",
    "custom_js": "portfolio/js/custom.js",
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"portfolio.Project": "vertical_tabs"},
    "language_chooser": True,
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
