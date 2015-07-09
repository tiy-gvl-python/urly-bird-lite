# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjectivity', '0002_bookmark_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='hashed',
            field=models.CharField(null=True, max_length=10),
        ),
    ]
