# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20171120_1452'),
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_quotes', to='login.User'),
        ),
    ]
