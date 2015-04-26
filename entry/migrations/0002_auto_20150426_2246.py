# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.AlterField(
            model_name='article',
            name='content_markup',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='entry.Tag', blank=True),
        ),
    ]
