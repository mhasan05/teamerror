# Generated by Django 4.2.6 on 2023-10-29 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name_plural': 'PACKAGE'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'ALL SERVICE'},
        ),
    ]
