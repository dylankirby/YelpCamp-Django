# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 19:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0017_auto_20171005_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 19, 40, 6, 271144, tzinfo=utc)),
        ),
    ]