# Generated by Django 3.1.4 on 2020-12-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20201226_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='abstraksiArtikel',
            field=models.TextField(max_length=360),
        ),
    ]
