# Generated by Django 4.0.9 on 2023-02-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='costo_total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fism',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='obra',
            name='inv_estatal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='obra',
            name='inv_federal',
            field=models.FloatField(),
        ),
    ]