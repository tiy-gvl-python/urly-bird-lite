# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjectivity', '0003_bookmark_hashed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clicker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('bookmark', models.ForeignKey(to='subjectivity.Bookmark')),
            ],
        ),
    ]
