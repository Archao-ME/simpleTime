# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_article_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author_id',
        ),
    ]
