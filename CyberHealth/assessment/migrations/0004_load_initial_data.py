# Generated by Django 3.1.7 on 2021-04-14 17:29

from django.core.management import call_command
from django.core.serializers import base, python
from django.db import migrations
import pathlib
import logging

logger = logging.getLogger(__name__)


def load_fixture(apps, schema_editor):
    # Save the old _get_model() function
    old_get_model = python._get_model

    # Define new _get_model() function here, which utilizes the apps argument to
    # get the historical version of a model. This piece of code is directly stolen
    # from django.core.serializers.python._get_model, unchanged. However, here it
    # has a different context, specifically, the apps variable.

    def _get_model(model_identifier):
        try:
            return apps.get_model(model_identifier)
        except (LookupError, TypeError):
            raise base.DeserializationError(
                "Invalid model identifier: '%s'" % model_identifier)

    # Replace the _get_model() function on the module, so loaddata can utilize it.
    python._get_model = _get_model
    try:
        # Call loaddata command
        fixture_files = list(pathlib.Path().glob('*/fixtures/0004*.json'))

        logger.info("%s fixture files", fixture_files)

        call_command('loaddata', *fixture_files, app_label='assessment')
    finally:
        # Restore old _get_model() function
        python._get_model = old_get_model


class Migration(migrations.Migration):
    dependencies = [
        ('assessment', '0003_auto_20210412_1509'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
