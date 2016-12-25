# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 22:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20160414_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 22, 20, 34, 233211, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 22, 20, 34, 233165, tzinfo=utc)),
        ),
    ]
