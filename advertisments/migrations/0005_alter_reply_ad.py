# Generated by Django 5.0.2 on 2024-02-13 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisments', '0004_alter_ad_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies_to_ad', to='advertisments.ad'),
        ),
    ]