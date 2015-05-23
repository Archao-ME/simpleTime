# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_ID', models.IntegerField()),
                ('song_Name', models.CharField(max_length=20)),
                ('user_ID', models.IntegerField()),
                ('date', models.CharField(max_length=12)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
