# Generated by Django 3.2.5 on 2022-09-12 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20220902_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.ManyToManyField(to='resources.ResourceCategory', verbose_name='Product Category'),
        ),
    ]
