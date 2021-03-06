# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WolfPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
    ]
