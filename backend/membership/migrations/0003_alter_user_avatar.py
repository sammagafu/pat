# Generated by Django 3.2.5 on 2022-11-16 10:23

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_alter_user_typeofmember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='default.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='profile/images/%Y/%m/%d', verbose_name='Profile Image'),
        ),
    ]