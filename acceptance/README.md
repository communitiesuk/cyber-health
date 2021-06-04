# MHCLG CyberHealth Documentation

The MHCLG Cyber Health Framework is a self-assessment tool to help Local Authorities understand their cyber resilience. 

This project uses node in order to run acceptance tests

# Before you start

To run this project you need:

- [Install Gulp, Node.JS and NPM](https://nodejs.org/en/)
- Run the [CyberHealth](../CyberHealth/README.md) application

## Installing dependencies

- run `npm install` for JavaScript dependencies

## Run tests
```
npm run test
```

# Troubleshooting

## To install test data
e.g. If your tests fail it might be worth testing whether you have installed the test data for acceptance or accessibility tests.

Run `python manage.py loaddata */fixtures/testdata*.json`

# Licence

Unless stated otherwise, the codebase is released under [the MIT License][mit].
This covers both the codebase and any sample code in the documentation.

The documentation is [© Crown copyright][copyright] and available under the terms of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
