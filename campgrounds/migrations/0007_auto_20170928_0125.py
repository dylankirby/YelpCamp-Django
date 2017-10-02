# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0006_auto_20170919_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campground',
            name='description',
        ),
        migrations.AddField(
            model_name='campground',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='campground',
            name='seasons',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')], default='Summer', max_length=6),
        ),
        migrations.AddField(
            model_name='campground',
            name='short_description',
            field=models.CharField(default='Campground', max_length=128),
        ),
    ]