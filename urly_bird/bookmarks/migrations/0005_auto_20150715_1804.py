# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0004_auto_20150709_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('hashed', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=150)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='click',
            name='user',
        ),
        migrations.DeleteModel(
            name='Click',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
