# Generated by Django 3.0.3 on 2020-05-31 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20200531_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
    ]
