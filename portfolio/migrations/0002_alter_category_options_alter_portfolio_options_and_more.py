# Generated by Django 4.2.6 on 2023-10-29 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'CATEGORY'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'PORTFOLIO'},
        ),
        migrations.AlterModelOptions(
            name='relatedimage',
            options={'verbose_name_plural': 'RELATED IMAGE'},
        ),
    ]