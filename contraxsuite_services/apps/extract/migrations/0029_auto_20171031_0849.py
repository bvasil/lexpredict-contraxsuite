# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract', '0028_citationusage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='type',
            field=models.CharField(blank=True, db_index=True, max_length=1024, null=True),
        ),
    ]
