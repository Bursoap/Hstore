HH Coding Task
==============

This is Hunted Hive coding task.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


How to set up this project?
===========================
The project has been built using cookiecutter-django template (https://github.com/pydanny/cookiecutter-django). Please refer to its docs for some more information. Also this project use PostgreSQL specific model HStoreField (https://docs.djangoproject.com/en/2.1/ref/contrib/postgres/fields/#hstorefield). Launching the project follows well known guidelines of setting up a standard django project:

- creating virtualenv
- installing requirements (local.txt)
- creating .env file your like .env-example in project root
- setting environment variable allowing django to read .env
- creating hstore extension for PostgreSQL
- running migrations
- running django dev server

Generic app
===========
This app provides:

- GenericModel which use HstoreField for storing any data.
- Simple create view
- ModelForm with mixin which use scheme(see below) describing data that GenericModel can store/process
- Admin panel with user friendly interface to create/edit GenericModel objects

Scheme
------

In generic app you can see a scheme module which provides GENERAL_SCHEME dict. Form use this dict for adding fields to form and saving to HstoreField. There are 3 required params for each field:

- field_name
- field_type
- kwargs

Use kwargs to add arguments for field, such as max_length, validators. For some fields kwargs can be optional.
