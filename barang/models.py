from django.db import models

# Create your models here.
class BarangModel(models.Model):
    idBarang = models.IntegerField()
    namaBarang = models.CharField(max_length = 50)
    deskripsiBarang = models.TextField()
    urlFoto = models.CharField(max_length = 50)
    hargaBarang = models.FloatField()
    jumlahStok = models.IntegerField()
    rating = models.FloatField()
    stokRate = models.IntegerField()