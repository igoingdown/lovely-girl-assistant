# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_auto_20170604_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historymessage',
            name='url_body',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]