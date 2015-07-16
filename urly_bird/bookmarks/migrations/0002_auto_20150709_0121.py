# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='click',
            old_name='bookmark',
            new_name='httpurl',
        ),
        migrations.RemoveField(
            model_name='click',
            name='id',
        ),
        migrations.AddField(
            model_name='click',
            name='short_id',
            field=models.SlugField(default=datetime.datetime(2015, 7, 9, 1, 21, 10, 100652), max_length=8, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
