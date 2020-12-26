from django.db import models

# Create your models here.
class LembagaSosialModel(models.Model):
    namaLs = models.TextField()
    deskripsi = models.TextField()
    urlFoto = models.TextField()
    namaPimpinan = models.TextField()
    jenis = models.TextField()
    kapasitas = models.TextField()
    kebutuhan = models.TextField()
    nomorTeleponLs = models.TextField()
    alamat = models.TextField()

class DonasiModel(models.Model):
    status = models.TextField()
    alasanPembatalan = models.TextField()
    jenisBarang = models.TextField()
    metodePengiriman = models.TextField()
    tanggalPengiriman = models.TextField()
    alamatJemput = models.TextField()
    namaDonatur = models.TextField()
    tanggalDonasi = models.TextField()
    lembagaSosial = models.ForeignKey(LembagaSosialModel, on_delete=models.CASCADE)