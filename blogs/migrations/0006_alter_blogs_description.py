# Generated by Django 4.1.6 on 2023-11-03 15:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_blogs_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]