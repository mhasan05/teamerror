# Generated by Django 4.2.6 on 2023-10-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='Soguna,Belkuchi', max_length=200)),
                ('city', models.CharField(default='Sirajganj', max_length=100)),
                ('country', models.CharField(default='Bangladesh', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
                ('facebook', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]