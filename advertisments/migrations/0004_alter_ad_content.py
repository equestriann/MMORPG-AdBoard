# Generated by Django 5.0 on 2023-12-08 23:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisments', '0003_alter_ad_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]