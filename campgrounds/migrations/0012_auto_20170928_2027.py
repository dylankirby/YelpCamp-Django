# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0011_auto_20170928_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campground',
            name='price_per_night',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]