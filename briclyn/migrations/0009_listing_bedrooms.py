# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('briclyn', '0008_auto_20160724_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
