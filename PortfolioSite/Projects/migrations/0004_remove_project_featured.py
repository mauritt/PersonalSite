# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_project_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='featured',
        ),
    ]
