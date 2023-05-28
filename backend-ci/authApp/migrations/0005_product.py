# Generated by Django 4.1.1 on 2022-09-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0004_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nameProduto', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('precio_unitario', models.FloatField()),
                ('talla', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]