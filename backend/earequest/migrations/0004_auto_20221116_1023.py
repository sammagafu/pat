# Generated by Django 3.2.5 on 2022-11-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earequest', '0003_auto_20221109_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityrequest',
            name='approveddate',
            field=models.DateField(verbose_name='Approved Date'),
        ),
        migrations.AlterField(
            model_name='activityrequest',
            name='requestdate',
            field=models.DateField(auto_now_add=True, verbose_name='Requesting Date'),
        ),
    ]
