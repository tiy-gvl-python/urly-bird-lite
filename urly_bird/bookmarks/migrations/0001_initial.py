# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('bookmark', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url_title', models.CharField(max_length=50)),
                ('url_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='click',
            name='user',
            field=models.ForeignKey(to='bookmarks.User'),
        ),
    ]
