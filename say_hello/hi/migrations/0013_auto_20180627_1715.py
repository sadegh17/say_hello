# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-27 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0012_auto_20180627_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faverest',
            name='addTime',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='faverest',
            name='upTime',
            field=models.TimeField(auto_now=True),
        ),
    ]
