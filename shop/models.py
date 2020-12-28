from django.db import models
from django.contrib.auth.models import User
from barang.models import Barang
from django.core.validators import MinValueValidator

# Create your models here.
class KeranjangModel(models.Model):
    def hitungTotal(self):
        total = 0
        for barang in self.barangkeranjang_set.all():
            total += barang.subtotal()
        return total

class BarangKeranjang(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    qty = models.IntegerField(validators=[MinValueValidator(1)])
    keranjang = models.ForeignKey(KeranjangModel, on_delete=models.CASCADE)

    def subtotal(self):
        return self.barang.hargaBarang * self.qty

class KontributorModel(models.Model):
    pengguna = models.OneToOneField(User, on_delete=models.CASCADE)
    urlFotoDiriDenganKtp = models.TextField()
    urlFotoKTP = models.TextField()
    keranjang = models.OneToOneField(KeranjangModel, on_delete=models.CASCADE, null=True, blank=True)

class TransaksiModel(models.Model):
    waktuDibuat = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    totalHarga = models.FloatField()
    metodePengiriman = models.CharField(max_length=10, null=True)
    kontributor = models.ForeignKey(KontributorModel, on_delete=models.CASCADE)

class BarangTrx(models.Model):
    barangTrx = models.ForeignKey(Barang, on_delete=models.CASCADE)
    qtyTrx = models.IntegerField(validators=[MinValueValidator(1)])
    transaksi = models.ForeignKey(TransaksiModel, on_delete=models.CASCADE)

    def subtotal(self):
        return self.barangTrx.hargaBarang * self.qtyTrx

class PembayaranModel(models.Model):
    waktuPembayaran = models.DateTimeField(auto_now_add=True)
    totalPembayaran = models.FloatField()
    transaksi = models.OneToOneField(TransaksiModel, on_delete=models.CASCADE)

class PengirimanModel(models.Model):
    namaEkspedisi = models.CharField(max_length=100)
    nomorResi = models.CharField(max_length=20)
    transaksi = models.OneToOneField(TransaksiModel, on_delete=models.CASCADE)