# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-24 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='b_or_v',
            new_name='custcategory',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='s_or_c',
            new_name='truckcategory',
        ),
        migrations.AlterField(
            model_name='quote',
            name='hours',
            field=models.IntegerField(),
        ),
    ]
