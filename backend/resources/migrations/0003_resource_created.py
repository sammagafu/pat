# Generated by Django 3.2.5 on 2022-08-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_resource_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Created at'),
        ),
    ]