# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishan', '0007_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='l',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='contact_no',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
    ]
