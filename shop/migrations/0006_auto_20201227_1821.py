# Generated by Django 3.1.4 on 2020-12-27 10:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_auto_20201227_0702'),
        ('shop', '0005_auto_20201227_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keranjangmodel',
            name='listBarang',
        ),
        migrations.CreateModel(
            name='BarangTransaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.barang')),
                ('keranjang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.keranjangmodel')),
            ],
        ),
    ]