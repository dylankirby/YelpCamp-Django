# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0003_auto_20170914_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campground',
            name='image',
            field=models.URLField(),
        ),
    ]