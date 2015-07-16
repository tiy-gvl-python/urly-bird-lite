# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenUrls',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('short_url', models.CharField(max_length=50)),
                ('long_url', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
