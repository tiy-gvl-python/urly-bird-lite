# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='click',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('used', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='Bookmark',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='Bookmark',
            name='description',
            field=models.CharField(blank=True, max_length=140, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='click',
            name='Bookmark',
            field=models.ForeignKey(to='urlshortner.models.Bookmark'),
        ),
    ]
