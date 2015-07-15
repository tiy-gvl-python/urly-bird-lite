# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('used', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.CharField(blank=True, max_length=140, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='shorturl',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='click',
            name='bookmark',
            field=models.ForeignKey(to='urlshortner.Bookmark'),
        ),
    ]
