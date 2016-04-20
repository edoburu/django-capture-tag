#!/usr/bin/env python
import sys
import django
from django.conf import settings, global_settings as default_settings
from django.core.management import execute_from_command_line
from os import path

if not settings.configured:
    module_root = path.dirname(path.realpath(__file__))

    sys.path.insert(0, path.join(module_root, 'example'))

    if django.VERSION >= (1, 8):
        template_settings = dict(
            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': (),
                    'OPTIONS': {
                        'loaders': (
                            'django.template.loaders.filesystem.Loader',
                            'django.template.loaders.app_directories.Loader',
                        ),
                        'context_processors': (
                            'django.template.context_processors.debug',
                            'django.template.context_processors.i18n',
                            'django.template.context_processors.media',
                            'django.template.context_processors.request',
                            'django.template.context_processors.static',
                            'django.contrib.auth.context_processors.auth',
                        ),
                    },
                },
            ]
        )
    else:
        template_settings = dict(
            TEMPLATE_LOADERS = (
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.filesystem.Loader',
            ),
            TEMPLATE_CONTEXT_PROCESSORS = list(default_settings.TEMPLATE_CONTEXT_PROCESSORS) + [
                'django.core.context_processors.request',
            ],
        )

    settings.configure(
        DEBUG = False,  # will be False anyway by DjangoTestRunner.
        TEMPLATE_DEBUG = True,
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        INSTALLED_APPS = (
            'capture_tag',
        ),
        TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner' if django.VERSION < (1, 6) else 'django.test.runner.DiscoverRunner',
        **template_settings
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'capture_tag'] + sys.argv[1:]
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
