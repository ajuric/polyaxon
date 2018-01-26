# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 12:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('memory', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('gpu', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
    ]
