# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-16 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='updated_ad',
            new_name='updated_at',
        ),
    ]