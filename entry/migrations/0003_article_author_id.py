# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20150426_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_id',
            field=models.IntegerField(default=datetime.datetime(2015, 4, 26, 15, 10, 39, 357297, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
