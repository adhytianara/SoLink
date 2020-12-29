from .models import *
from barang.models import Barang
from shop.models import TransaksiModel
from shop.Kontributor import Transaksi

class Mitra:

    def __init__(self,namaPemilik):
        self.namaPemilik = namaPemilik
        self.barang = Barang.objects.all().filter(namaPemilik=namaPemilik)
        self.jamBuka = "08:00"
        self.hariBuka = "Senin - Jumat"
        self.nomorRekeningBank = "1806141126141441"
        self.npwp = "18061411266211"
        self.urlSuratUsaha = "https://ecs7.tokopedia.net/img/cache/700/VqbcmM/2020/7/19/2b89cbf4-36ee-4cde-9d21-14c0413be050.jpg"
        self.ktp = "1806141126"
        self.id = 0
        self.transaksi = {}
    
    def menambahkanBarang(self,barangBaru):
        barangBaru.save()
    
    def menghapusBarang(self,id):
        b = Barang.objects.get(namaPemilik=self.namaPemilik,idBarang=id)
        b.delete()
    
    def getSuatuBarang(self,id):
        return Barang.objects.get(idBarang=id)

    def barangMitra(self):
        return self.barang
    
    def konfirmasiTransaksi(self, idTrx):
        self.trxDBsync()
        trx = self.transaksi[int(idTrx)]
        trx.ubahStatus("Sedang Dikemas")
    
    def batalkanTransaksi(self, idTrx):
        self.trxDBsync()
        trx = self.transaksi[int(idTrx)]
        trx.ubahStatus("Dibatalkan")

    def getTransaksi(self, id):
        self.trxDBsync()
        return self.transaksi[id]

    def trxDBsync(self):
        for el in TransaksiModel.objects.all():
            self.transaksi[el.id] = Transaksi(el)