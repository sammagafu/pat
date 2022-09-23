# Generated by Django 3.2.5 on 2022-09-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Title')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='Slug')),
                ('cover', models.ImageField(upload_to='blog/covers/', verbose_name='Cover Image')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('downloads', models.IntegerField(default=0, editable=False, verbose_name='Number Of Views')),
                ('membersonly', models.BooleanField(default=False, verbose_name='Members only')),
            ],
            options={
                'verbose_name': 'Updates',
                'verbose_name_plural': 'Updatess',
            },
        ),
    ]
