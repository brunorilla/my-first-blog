# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='color',
            field=models.CharField(default=datetime.datetime(2017, 12, 15, 18, 46, 18, 227558, tzinfo=utc), max_length=60),
            preserve_default=False,
        ),
    ]
