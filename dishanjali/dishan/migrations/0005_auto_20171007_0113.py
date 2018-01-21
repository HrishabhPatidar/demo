# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishan', '0004_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='contact_no',
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=20000),
        ),
    ]
