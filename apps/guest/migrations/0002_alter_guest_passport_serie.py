# Generated by Django 4.2.8 on 2024-03-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='passport_serie',
            field=models.CharField(max_length=7, verbose_name='Passport serie'),
        ),
    ]