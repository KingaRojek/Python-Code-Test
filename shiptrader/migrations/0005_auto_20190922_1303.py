# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('shiptrader', '0004_listing_is_active')]

    operations = [
        migrations.AlterField(
            model_name='starship',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        )
    ]
