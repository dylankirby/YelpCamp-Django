# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 05:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0005_auto_20170919_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campground',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_campgrounds', to=settings.AUTH_USER_MODEL),
        ),
    ]