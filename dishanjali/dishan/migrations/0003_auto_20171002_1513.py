# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishan', '0002_registrationdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='discription',
            field=models.CharField(max_length=150),
        ),
    ]
