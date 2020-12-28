from .models import *
from barang.models import Barang

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
        # ubah jangan lupa import
        # self.transaksi = Transaksi.objects.all().filter(namaPemilik=namaPemilik)
    
    def menambahkanBarang(self,barangBaru):
        barangBaru.save()
    
    def menghapusBarang(self,id):
        b = Barang.objects.get(namaPemilik=self.namaPemilik,idBarang=id)
        b.delete()
    
    def getSuatuBarang(self,id):
        return Barang.objects.get(idBarang=id)

    def barangMitra(self):
        return self.barang
    
    # def konfirmasiTransaksi(self):
    #     return
    
    # def batalkanTransaksi(self):
    #     return
    
    # def inputPengiriman(self):
    #     return
