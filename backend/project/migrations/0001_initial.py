# Generated by Django 3.2.5 on 2022-08-30 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='project/cover/', verbose_name='Project Cover Image')),
                ('projectname', models.CharField(max_length=150, verbose_name='Project Name')),
                ('startdate', models.DateField(verbose_name='Starting Date')),
                ('shortdescription', models.TextField(verbose_name='Short Description')),
                ('specificObjective', models.TextField(verbose_name='Specific Objective')),
                ('enddate', models.DateField(verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(verbose_name='Donors Website')),
                ('donors', models.ImageField(upload_to='donors/logo/', verbose_name='Donors Logo')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=150, verbose_name='Project Goal')),
                ('results', models.CharField(max_length=180, verbose_name='Project Result')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='')),
            ],
            options={
                'verbose_name': 'project goal',
                'verbose_name_plural': 'project goals',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.projectdonor', verbose_name=''),
        ),
    ]
