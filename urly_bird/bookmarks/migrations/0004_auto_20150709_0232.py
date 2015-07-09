# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20150709_0124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='url_title',
            new_name='title_bookmark',
        ),
    ]
