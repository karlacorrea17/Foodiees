# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0011_pedido_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='idRest',
        ),
        migrations.AddField(
            model_name='producto',
            name='idPro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Restaurante'),
        ),
    ]
