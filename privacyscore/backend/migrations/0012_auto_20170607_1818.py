# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20170604_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='end',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]