# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_auto_20170405_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans_form_business',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='loans_form_mortgage',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]