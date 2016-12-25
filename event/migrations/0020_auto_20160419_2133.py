# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 21:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0019_auto_20160419_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postevent',
            name='participate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 21, 33, 47, 859747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 21, 33, 47, 859716, tzinfo=utc)),
        ),
    ]
