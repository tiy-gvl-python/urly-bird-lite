# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=140, blank=True)),
            ],
        ),
    ]
