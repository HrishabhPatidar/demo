# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='reg_detail')),
            ],
        ),
    ]
