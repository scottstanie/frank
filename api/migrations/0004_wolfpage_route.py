# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160524_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='wolfpage',
            name='route',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
