import sys
import time

bust = {"bust": time.time()}

CONFIGURABLE_OPTIONS = [
    "--db",
    "--cms-version",
    "--django-version",
    "--i18n",
    "--reversion",
    "--languages",
    "--timezone",
    "--use-tz",
    "--permissions",
    "--bootstrap",
    "--templates",
    "--starting-page",
]

DJANGOCMS_DEVELOP = "https://github.com/yakky/django-cms/archive/develop.zip?{bust}".format(**bust)
DJANGOCMS_RC = "https://github.com/divio/django-cms/archive/release/3.7.x.zip?{bust}".format(**bust)
DJANGOCMS_BETA = DJANGOCMS_RC
DJANGOCMS_37 = "django-cms>=3.7,<3.8"

DJANGOCMS_SUPPORTED = ("3.7", "stable", "lts", "develop", "rc")
DJANGOCMS_STABLE = "3.7"
DJANGOCMS_LTS = "3.7"
DJANGOCMS_DEFAULT = DJANGOCMS_STABLE

DJANGO_DEVELOP = "https://github.com/django/django/archive/master.zip?{bust}".format(**bust)
DJANGO_BETA = "https://github.com/django/django/archive/master.zip?{bust}".format(**bust)
if sys.version_info >= (3, 6):
    DJANGO_SUPPORTED = ("2.2", "3.0", "stable", "lts")
    DJANGO_STABLE = "3.0"
    DJANGO_LTS = "2.2"
else:
    DJANGO_SUPPORTED = ("2.2", "stable", "lts")
    DJANGO_STABLE = "2.2"
    DJANGO_LTS = "2.2"

DJANGO_DEFAULT = DJANGO_STABLE

CMS_VERSION_MATRIX = {
    "stable": DJANGOCMS_STABLE,
    "lts": DJANGOCMS_LTS,
    "rc": DJANGOCMS_RC,
    "beta": DJANGOCMS_BETA,
    "develop": DJANGOCMS_DEVELOP,
}
DJANGO_VERSION_MATRIX = {
    "stable": DJANGO_STABLE,
    "lts": DJANGO_LTS,
    "rc": DJANGO_STABLE,
    "beta": DJANGO_STABLE,
    "develop": DJANGO_STABLE,
}
VERSION_MATRIX = {
    "3.7": ("2.2", "3.0"),
    DJANGOCMS_BETA: ("2.2", "3.0"),
    DJANGOCMS_RC: ("2.2", "3.0"),
    DJANGOCMS_DEVELOP: ("2.2", "3.0"),
}
PACKAGE_MATRIX = {
    "3.7": DJANGOCMS_37,
    DJANGOCMS_RC: DJANGOCMS_RC,
    DJANGOCMS_BETA: DJANGOCMS_BETA,
    DJANGOCMS_DEVELOP: DJANGOCMS_DEVELOP,
}

REQUIREMENTS = {
    "default": ["html5lib>=1.0.1", "Pillow>=3.0", "six", "pytz"],
    "django-2.2": ["django-classy-tags>=0.9", "django-sekizai>=1.0", "django-mptt>0.9"],
    "django-3.0": ["django-classy-tags>=0.9", "django-sekizai>=1.0", "django-mptt>0.9"],
    "cms-3.7": ["djangocms-admin-style>=1.5,<1.6", "django-treebeard>=4.0,<5.0"],
    "cms-master": [
        "https://github.com/divio/djangocms-admin-style/archive/master.zip?{bust}".format(**bust),
        "django-treebeard>=4.0,<5.0",
    ],
    "plugins-3.7": [
        "djangocms-text-ckeditor>=3.7,<4.0",
        "djangocms-link>=2.5,<2.7",
        "djangocms-icon>=1.4,<1.6",
        "djangocms-style>=2.2,<2.4",
        "djangocms-googlemap>=1.3,<1.5",
        "djangocms-snippet>=2.2,<2.4",
        "djangocms-video>=2.1,<2.4",
        "djangocms-file>=2.3,<2.5",
        "djangocms-picture>=2.3,<2.5",
        "djangocms-bootstrap4>=1.5,<1.7",
    ],
    "plugins-master": [
        "https://github.com/divio/djangocms-text-ckeditor/archive/master.zip?{bust}" "".format(**bust),
        "https://github.com/divio/djangocms-file/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-link/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-icon/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-style/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-googlemap/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-snippet/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-picture/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-video/archive/master.zip?{bust}".format(**bust),
        "https://github.com/divio/djangocms-bootstrap4/archive/master.zip?{bust}".format(**bust),
    ],
    "plugins-basic": [],
    "plugins-basic-master": [],
    "filer": ["easy_thumbnails", "django-filer>=1.3"],
}

TEMPLATES_1_8 = """
TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [{dirs}],
        'OPTIONS': {{
            'context_processors': [
                {processors}
            ],
            'loaders': [
                {loaders}
            ],
        }},
    }},
]
"""

PLUGIN_LIST_TEXT = """
djangocms installer will install and configure the following plugins:
 * djangocms-text-ckeditor (Text plugin)
 * djangocms-link (Link plugin)
 * djangocms-file (File plugin)
 * djangocms-picture (Image plugin)
 * djangocms-style (Style plugin)
 * djangocms-snippet (Snippet plugin)
 * djangocms-googlemap (GoogleMap plugin)
 * djangocms-video (Video plugin)
"""

DRIVERS = {
    "django.db.backends.postgresql": "psycopg2",
    "django.db.backends.postgresql_psycopg2": "psycopg2",
    "django.contrib.gis.db.backends.postgis": "postgis",
    "django.db.backends.postgresql_postgis": "postgis",
    "django.db.backends.mysql": "mysqlclient",
    "django.db.backends.sqlite3": "",
}

DEFAULT_PROJECT_HEADER = """# -*- coding: utf-8 -*-
import os  # isort:skip
gettext = lambda s: s
"""
STATICFILES_DEFAULT = """STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)"""

BASE_DIR = """
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
"""

VERSION_WARNING = "{0} version of {1} is not supported and it may not work as expected"
