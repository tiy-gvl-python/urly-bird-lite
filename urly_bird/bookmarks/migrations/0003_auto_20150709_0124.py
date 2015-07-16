# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20150709_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='click',
            old_name='httpurl',
            new_name='http_url',
        ),
    ]
