# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 03:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20170223_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlog',
            name='asset_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Asset'),
        ),
    ]
