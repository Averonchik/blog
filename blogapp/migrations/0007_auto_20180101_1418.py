# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-01 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20180101_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='subscribers',
            field=models.ManyToManyField(related_name='subs', to='blogapp.ProfileUser'),
        ),
    ]
