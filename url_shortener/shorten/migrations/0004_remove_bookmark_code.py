# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0003_auto_20150715_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='code',
        ),
    ]
