from django.db import models

# Create your models here.
class Barang(models.Model):
    namaPemilik = models.CharField(max_length = 50)
    idBarang = models.IntegerField()
    namaBarang = models.CharField(max_length = 50)
    deskripsiBarang = models.TextField()
    urlFoto = models.CharField(max_length = 50)
    hargaBarang = models.FloatField()
    jumlahStok = models.IntegerField()
    rating = models.FloatField()
    stokRate = models.IntegerField()

    def updateNama(self,nama):
        self.update
    
    def updateDeskripsi(self,deksripsi):
        self.deskripsiBarang = deksripsi
    