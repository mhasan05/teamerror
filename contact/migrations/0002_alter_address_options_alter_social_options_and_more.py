# Generated by Django 4.2.6 on 2023-10-29 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'ADDRESS'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'SOCIAL LINK'},
        ),
        migrations.AlterModelOptions(
            name='support',
            options={'verbose_name_plural': 'SUPPORT MESSAGE'},
        ),
    ]
