# Generated by Django 4.1.6 on 2023-11-07 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolio_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
    ]