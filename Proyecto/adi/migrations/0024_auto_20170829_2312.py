# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-29 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0023_auto_20170829_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='alumno',
            field=models.ForeignKey(default=543, on_delete=django.db.models.deletion.CASCADE, to='adi.Alumno'),
            preserve_default=False,
        ),
    ]
