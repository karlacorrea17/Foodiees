# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0010_auto_20160808_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='Cliente',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
