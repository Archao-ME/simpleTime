# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20150427_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.IntegerField(default=1),
        ),
    ]
