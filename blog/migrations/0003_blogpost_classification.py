# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160403_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='classification',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
