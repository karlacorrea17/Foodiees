# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 03:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appfoodie', '0016_auto_20160810_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='idPedi',
            new_name='idPed',
        ),
    ]
