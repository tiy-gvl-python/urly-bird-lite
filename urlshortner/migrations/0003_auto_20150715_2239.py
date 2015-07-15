# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0002_auto_20150715_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='shorturl',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
