# README

A basic Django application demonstrating a parent child foreign key relationship.

To run (once Django installed):
- ./manage.py makemigrations
- ./manage.py migrate
- ./manage.py createsuperuser
- ./manage.py runserver

To run tests use:

- ./manage test

This application also be deployed on Heroku. To run locally you will need the settings:

- SECRET_KEY='<your_secret_key>'
- ALLOWED_HOST=''
- DJANGO_SETTINGS_MODULE=django_parent_child.local_settings

then run 'heroku local web'.

To deploy to Heroku (once you have an account):

- heroku create
- heroku login
- git push heroku master

then login to your dashboard and:

- Add a config var for ALLOWED_HOST
- Add a config var for SECRET_KEY
- Create a postgres add-on for the application

and from the command line:

- heroku run bash
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- exit