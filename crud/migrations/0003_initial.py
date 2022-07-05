# Generated by Django 4.0.5 on 2022-07-05 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crud', '0002_remove_producto_marca_delete_marca_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de la categoria')),
                ('categoria', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['idCategoria'],
            },
        ),
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('idRemedio', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Id remedio')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción del remedio')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='Remedios', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.categoria')),
            ],
            options={
                'verbose_name': 'Remedio',
                'verbose_name_plural': 'Remedios',
                'ordering': ['idRemedio'],
            },
        ),
    ]
