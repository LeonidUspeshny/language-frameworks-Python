# Generated by Django 5.0.6 on 2024-08-04 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_merge_20240804_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
    ]
