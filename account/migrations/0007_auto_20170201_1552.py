# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20170201_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='static/images/no-img.jpg', upload_to='users/%Y/%m/%d'),
        ),
    ]
