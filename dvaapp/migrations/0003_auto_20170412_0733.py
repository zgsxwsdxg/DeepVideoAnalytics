# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0002_s3_export'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='S3_Export',
            new_name='S3Export',
        ),
    ]
