# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0010_remove_repairs_repair_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
