# Generated by Django 4.0.6 on 2022-08-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projectspent',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('creator', models.CharField(blank=True, max_length=255, null=True)),
                ('spent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('spent_txt', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'projectspent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userspent',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('spent', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('spent_txt', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'userspent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userspentonprojects',
            fields=[
                ('project', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('issue', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('spent', models.TextField(blank=True, null=True)),
                ('date_spent', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'userspentonprojects',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Issues',
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.DeleteModel(
            name='Timelogs',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]