# Generated by Django 4.2.6 on 2023-10-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_address_options_alter_social_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'SOCIAL USERNAME'},
        ),
        migrations.AlterField(
            model_name='social',
            name='facebook',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='social',
            name='github',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='social',
            name='linkedin',
            field=models.CharField(max_length=50),
        ),
    ]
