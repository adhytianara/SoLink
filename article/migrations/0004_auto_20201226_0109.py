# Generated by Django 3.1.4 on 2020-12-25 18:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_artikel_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isiArtikel',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]