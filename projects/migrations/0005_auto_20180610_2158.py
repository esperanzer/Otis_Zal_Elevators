# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180610_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installations',
            name='name',
            field=models.CharField(help_text='Installation Name', max_length=100),
        ),
    ]
