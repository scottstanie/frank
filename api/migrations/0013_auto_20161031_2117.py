# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-31 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20160819_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='first_name',
            new_name='fb_source_user_id',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='last_name',
            new_name='full_name',
        ),
        migrations.AlterField(
            model_name='friend',
            name='invite_friend_id',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]