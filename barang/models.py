from django.db import models

# Create your models here.
class Barang(models.Model):
    namaPemilik = models.CharField(max_length = 50)
    idBarang = models.IntegerField()
    namaBarang = models.CharField(max_length = 50)
    deskripsiBarang = models.TextField()
    urlFoto = models.URLField(max_length=200)
    hargaBarang = models.FloatField()
    jumlahStok = models.IntegerField()
    rating = models.FloatField()
    stokRate = models.IntegerField()

    def updateNama(self,nama):
        self.namaBarang = nama
        self.save()
    
    def updateDeskripsi(self,deksripsi):
        self.deskripsiBarang = deksripsi
        self.save()

    def updateFoto(self,urlFoto):
        self.urlFoto =urlFoto
        self.save()
    
    def updateHarga(self,harga):
        self.hargaBarang = harga
        self.save()
    
    def tambahPenilaianRating(self,rate):
        newRating = self.stokRate *self.rating + rate
        self.rating = newRating/(self.stokRate + 1)
        self.stokRate += 1
        self.save()
    
    def getJumlahStok(self):
        return self.jumlahStok
    
    def updateJumlahStok(self,stok):
        self.jumlahStok = stok
        self.save()
