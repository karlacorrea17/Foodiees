# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0014_auto_20160810_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='idCli',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Cliente'),
        ),
    ]
