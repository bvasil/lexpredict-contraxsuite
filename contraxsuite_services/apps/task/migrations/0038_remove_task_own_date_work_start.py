# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-22 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0037_auto_20180822_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='own_date_work_start',
        ),
    ]