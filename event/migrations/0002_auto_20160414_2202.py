# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 22:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='postevent',
            name='city',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='postevent',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='postevent',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='postevent',
            name='state',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
