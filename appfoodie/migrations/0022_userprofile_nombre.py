# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0021_auto_20160810_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Nombre',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
