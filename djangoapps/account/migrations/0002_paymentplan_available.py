# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentplan',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]