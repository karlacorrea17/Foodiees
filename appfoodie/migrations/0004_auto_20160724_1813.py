# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-24 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0003_auto_20160724_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='idPedi',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Restaurante'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='idRest',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Producto'),
        ),
    ]