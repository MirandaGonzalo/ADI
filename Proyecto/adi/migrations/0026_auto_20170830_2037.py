# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-30 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0025_auto_20170830_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario2',
            name='preceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adi.Preceptor'),
        ),
        migrations.AlterField(
            model_name='formulario3',
            name='preceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adi.Preceptor'),
        ),
    ]
