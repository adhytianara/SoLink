# Generated by Django 3.1.4 on 2020-12-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarangModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBarang', models.IntegerField()),
                ('namaBarang', models.CharField(max_length=50)),
                ('deskripsiBarang', models.TextField()),
                ('urlFoto', models.CharField(max_length=50)),
                ('hargaBarang', models.FloatField()),
                ('jumlahStok', models.IntegerField()),
                ('rating', models.FloatField()),
                ('stokRate', models.IntegerField()),
            ],
        ),
    ]