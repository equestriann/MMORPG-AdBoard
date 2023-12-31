# Generated by Django 5.0 on 2023-12-06 16:19

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='До 255 символов', max_length=255)),
                ('category', models.CharField(choices=[('Tank', 'Tank'), ('Healer', 'Healer'), ('Damage dealer', 'Damage dealer'), ('Trader', 'Trader'), ('Guild master', 'Guild master'), ('Quest giver', 'Quest giver'), ('Warsmith', 'Warsmith'), ('Tanner', 'Tanner'), ('Potion maker', 'Potion maker'), ('Spell master', 'Spell master')], default=None, max_length=13)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisments.ad')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отклик',
                'verbose_name_plural': 'Отклики',
                'ordering': ['date_sent'],
            },
        ),
    ]
