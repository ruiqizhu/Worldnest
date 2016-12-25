# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 23:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20160414_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postevent',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='postevent',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 23, 43, 55, 520422, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='image',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 23, 43, 55, 520387, tzinfo=utc)),
        ),
    ]
