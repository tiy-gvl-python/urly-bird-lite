# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly', '0002_auto_20150715_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='shortened_url',
            new_name='hash',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
