# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishan', '0013_auto_20171013_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(default='10', max_length=254),
        ),
    ]
