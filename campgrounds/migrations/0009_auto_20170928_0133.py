# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 01:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0008_auto_20170928_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campground',
            name='price',
        ),
        migrations.RemoveField(
            model_name='campground',
            name='seasons',
        ),
    ]
