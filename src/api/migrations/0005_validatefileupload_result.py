# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comparefileupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='validatefileupload',
            name='result',
            field=models.CharField(default='old', max_length=128),
            preserve_default=False,
        ),
    ]