# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-27 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0011_auto_20180627_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faverest',
            name='date',
        ),
        migrations.RemoveField(
            model_name='faverest',
            name='image',
        ),
        migrations.AddField(
            model_name='faverest',
            name='addTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faverest',
            name='upTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]