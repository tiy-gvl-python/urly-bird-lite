# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='orig_url',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='link',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(null=True, max_length=20),
        ),
    ]
