# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_article_updatetime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.AlterField(
            model_name='article',
            name='createtime',
            field=models.DateTimeField(blank=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]
