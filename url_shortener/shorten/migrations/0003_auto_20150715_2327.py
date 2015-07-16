# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_auto_20150715_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
