# MHCLG CyberHealth Documentation

The MHCLG Cyber Health Framework is a self-assessment tool to help Local Authorities understand their cyber resilience. 

This project uses Django, which is a Python framework for building web applications. 

## Before you start

To run this project you need:

- [Install Gulp, Node.JS and NPM](https://nodejs.org/en/)
- [Install Python 3.7 or greater]()
- Install Postgres ( Consider `brew install` or your package manager )

## Installing dependencies

- run `pip3 install` for Python dependencies
- run `npm install` for JavaScript dependencies

## Publish static files
```
npm run frontend:build
npm run frontend:watch
```
## Preview your changes locally

Run `python manage.py runserver` 

## To run your tests

Run `python manage.py test` 

## To install your database

Run `python manage.py migrate` 

## To install test data
e.g., for acceptance or accessibility tests.

Run `python manage.py loaddata */fixtures/testdata*.json`

## Set environments variables on the terminal
```
PYTHONUNBUFFERED=1;
DJANGO_SETTINGS_MODULE=CyberHealth.settings;
SECRET_KEY=THIS_IS_A_SECRET_CHANGE_ME;
DJANGO_DEBUG=True;
DATABASE_URL=psql://database_user:database_pass@127.0.0.1:5432/database_name; 
GOVUK_NOTIFY_DISABLE=True (only to run acceptance tests)  
```

## Licence

Unless stated otherwise, the codebase is released under [the MIT License][mit].
This covers both the codebase and any sample code in the documentation.

The documentation is [© Crown copyright][copyright] and available under the terms of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/