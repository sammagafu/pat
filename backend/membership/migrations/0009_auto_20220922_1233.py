# Generated by Django 3.2.5 on 2022-09-22 12:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_auto_20220922_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mctnumber',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='MCT Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
