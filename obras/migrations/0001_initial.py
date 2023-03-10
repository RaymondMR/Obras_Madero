# Generated by Django 4.0.9 on 2023-02-26 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_comunidad', models.CharField(max_length=200)),
                ('rubro', models.CharField(max_length=60)),
                ('subclasificacion', models.CharField(max_length=40)),
                ('nombre_obra', models.CharField(max_length=200)),
                ('tenencia', models.CharField(max_length=30)),
                ('modalidad_ejecucion', models.CharField(max_length=17)),
                ('metas_cantidad', models.PositiveIntegerField()),
                ('metas_unidad', models.CharField(max_length=10)),
                ('metas_beneficiarios', models.PositiveIntegerField()),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('inv_estatal', models.DecimalField(decimal_places=2, max_digits=12)),
                ('inv_federal', models.DecimalField(decimal_places=2, max_digits=12)),
                ('fism', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
