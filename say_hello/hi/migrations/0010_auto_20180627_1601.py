# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-27 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0009_auto_20180627_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faverest',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='faverest',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]