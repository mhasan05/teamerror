# Generated by Django 4.2.6 on 2023-10-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_category_options_alter_portfolio_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='duration',
            field=models.CharField(max_length=30),
        ),
    ]
