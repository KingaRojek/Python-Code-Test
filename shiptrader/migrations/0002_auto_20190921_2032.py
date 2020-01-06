# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('shiptrader', '0001_initial')]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='cargo_capacity',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='starship', name='crew', field=models.IntegerField(null=True)
        ),
        migrations.AlterField(
            model_name='starship',
            name='hyperdrive_rating',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='starship', name='length', field=models.FloatField(null=True)
        ),
        migrations.AlterField(
            model_name='starship',
            name='passengers',
            field=models.IntegerField(null=True),
        ),
    ]
