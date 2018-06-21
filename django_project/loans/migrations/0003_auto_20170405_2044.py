# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 20:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_aboutusposts_homeinfoposts_howitworkposts_lendingpolicyposts_loans_form_business_loans_form_mortgage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loans_form_mortgage',
            old_name='Home_Phone',
            new_name='Contact_Number',
        ),
        migrations.RemoveField(
            model_name='loans_form_mortgage',
            name='Work_Phone',
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='Business_Contact',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message=b"# must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='Business_Zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message=b"Zip code must be entered in the format: '99999'. Up to 5 digits allowed.", regex=b'^\\+?1?\\d{0,5}$')]),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='DBA',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='Email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='Federal_Tax_ID_Number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='State_Tax_ID_Number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='Website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='loans_form_business',
            name='Zip_Code',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message=b"Zip code must be entered in the format: '99999'. Up to 5 digits allowed.", regex=b'^\\+?1?\\d{0,5}$')]),
        ),
        migrations.AlterField(
            model_name='loans_form_mortgage',
            name='Email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='loans_form_mortgage',
            name='Zip_Code',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message=b"Zip code must be entered in the format: '99999'. Up to 5 digits allowed.", regex=b'^\\+?1?\\d{0,5}$')]),
        ),
        migrations.AlterField(
            model_name='loans_form_mortgage',
            name='property_zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message=b"Zip code must be entered in the format: '99999'. Up to 5 digits allowed.", regex=b'^\\+?1?\\d{0,5}$')]),
        ),
    ]
