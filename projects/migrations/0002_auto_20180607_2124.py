# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenses',
            old_name='company_name',
            new_name='customer',
        ),
        migrations.AddField(
            model_name='expenses',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
