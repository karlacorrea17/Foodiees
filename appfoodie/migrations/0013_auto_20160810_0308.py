# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0012_auto_20160808_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='idPedi',
            new_name='idPro',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='idPro',
            new_name='idRes',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='Cliente',
        ),
        migrations.AddField(
            model_name='pedido',
            name='idCli',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appfoodie.Cliente'),
        ),
    ]