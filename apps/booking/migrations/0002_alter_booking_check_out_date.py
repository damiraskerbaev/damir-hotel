# Generated by Django 4.2.8 on 2024-03-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(verbose_name='Check out date'),
        ),
    ]