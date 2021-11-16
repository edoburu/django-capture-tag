#!/usr/bin/env python
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            },
        },
        SITE_ID=1,
        INSTALLED_APPS=("capture_tag",),
        MIDDLEWARE=(),
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": (),
                "OPTIONS": {
                    "loaders": ("django.template.loaders.filesystem.Loader",),
                    "context_processors": (),
                },
            },
        ],
        TEST_RUNNER="django.test.runner.DiscoverRunner",
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    )

DEFAULT_TEST_APPS = [
    "capture_tag",
]


def runtests():
    other_args = list(filter(lambda arg: arg.startswith("-"), sys.argv[1:]))
    test_apps = (
        list(filter(lambda arg: not arg.startswith("-"), sys.argv[1:])) or DEFAULT_TEST_APPS
    )
    argv = sys.argv[:1] + ["test", "--traceback"] + other_args + test_apps
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
