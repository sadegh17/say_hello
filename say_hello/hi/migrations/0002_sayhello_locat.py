# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-11 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sayhello',
            name='locat',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
