django-capture-tag
==================

.. image:: https://img.shields.io/travis/edoburu/django-capture-tag/master.svg?branch=master
    :target: http://travis-ci.org/edoburu/django-capture-tag
.. image:: https://img.shields.io/pypi/v/django-capture-tag.svg
    :target: https://pypi.python.org/pypi/django-capture-tag/
.. image:: https://img.shields.io/pypi/l/django-capture-tag.svg
    :target: https://pypi.python.org/pypi/django-capture-tag/
.. image:: https://img.shields.io/codecov/c/github/edoburu/django-capture-tag/master.svg
    :target: https://codecov.io/github/edoburu/django-capture-tag?branch=master

A micro-library to capture output in Django templates.

This can be useful for example to:

* Repeat page titles in web pages, e.g. for the ``<title>`` tag and breadcrumb.
* Repeat contents for Social Media tags.
* Reusing thumbnail output in multiple places.
* Fetch configuration data from extended templates.


Installation
------------

Install the module from PyPI:

.. code-block:: bash

    pip install django-capture-tag

Add the package to ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'capture_tag',
    )

Load the tag in your template:

.. code-block:: html+django

    {% load capture_tags %}


Syntax
------

The following options are available:

.. code-block:: html+django

    {% capture %}...{% endcapture %}                    # output in {{ capture }}
    {% capture silent %}...{% endcapture %}             # output in {{ capture }} only
    {% capture as varname %}...{% endcapture %}         # output in {{ varname }}
    {% capture as varname silent %}...{% endcapture %}  # output in {{ varname }} only


Example usage
-------------

To capture Social Media tags:

.. code-block:: html+django

    {% load capture_tags %}

    <head>
        ...

        {# Allow templates to override the page title/description #}
        <meta name="description" content="{% capture as meta_description %}{% block meta-description %}{% endblock %}{% endcapture %}" />
        <title>{% capture as meta_title %}{% block meta-title %}Untitled{% endblock %}{% endcapture %}</title>

        {# display the same value as default, but allow templates to override it. #}
        <meta property="og:description" content="{% block og-description %}{{ meta_description }}{% endblock %}" />
        <meta name="twitter:title" content="{% block twitter-title %}{{ meta_title }}{% endblock %}" />
    </head>

Take configuration from extended templates:

.. code-block:: html+django

    # base.html

    {% load capture_tags %}

    # read once
    {% capture as home_url silent %}{% block home_url %}{% url 'app:index' %}{% endblock %}{% endcapture %}

    # reuse twice.
    <a href="{{ home_url }}" class="btn page-top">Back to home</a>
    <a href="{{ home_url }}" class="btn page-bottom">Back to home</a>

    # child.html
    {% extends "base.html" %}

    {% block home_url %}{% url 'user:profile' %}{% endblock %}

Notice
~~~~~~

When a value is used only once, this package is not needed.
In such case, simply place the ``{% block .. %}`` at the proper location where contents is replaced.
All common Django template tags support the ``as variable`` syntax,
such as ``{% url 'app:index' as home_url %}`` or ``{% trans "Foo" as foo_label %}``.
