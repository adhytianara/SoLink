from loginin.Pengguna import Pengguna
from .models import KeranjangModel, BarangKeranjang, BarangTrx, TransaksiModel, PembayaranModel, PengirimanModel
from barang.models import Barang

class Keranjang:
    def __init__(self, keranjangModel):
        self.__keranjangModel = keranjangModel
    def addBarang(self, idBarang, qty=1):
        barang = Barang.objects.get(idBarang=idBarang)
        barangKrjg = BarangKeranjang(barang=barang, qty=qty, keranjang=self.__keranjangModel)
        barangKrjg.save()
        return barang.namaBarang
    def hitungTotal(self):
        return self.__keranjangModel.hitungTotal()
    def getModel(self):
        return self.__keranjangModel

class Kontributor(Pengguna):
    def __init__(self, kontributorModel, *args):
        Pengguna.__init__(self, *args)
        self.__kontributorModel = kontributorModel
        self.__urlFotoDiriDenganKtp = kontributorModel.urlFotoDiriDenganKtp
        self.__urlFotoKTP = kontributorModel.urlFotoKTP
        self.__keranjang = Keranjang(kontributorModel.keranjang)
        self.__listTransaksi = {}
    def getModel(self):
        return self.__kontributorModel
    def tambahBarangKeranjang(self, idBarang):
        return self.__keranjang.addBarang(idBarang)
    def getKeranjang(self):
        return self.__keranjang
    def createTransaksi(self, totalHarga, metodePengiriman, kontributorModel, mitra):
        trxModel = TransaksiModel(status="Menunggu Pembayaran", totalHarga=totalHarga, metodePengiriman=metodePengiriman, kontributor=kontributorModel)
        trxModel.save()
        trx = Transaksi(trxModel)
        self.__listTransaksi[trx.getId()] = trx
        mitra.transaksi[trx.getId()] = trx

        listQty = {}
        listModel = {}
        for el in self.__keranjang.getModel().barangkeranjang_set.all():
            namaBarang = el.barang.namaBarang
            if namaBarang in listModel.keys():
                listQty[namaBarang] += 1
            else:
                listQty[namaBarang] = 1
                listModel[namaBarang] = el.barang
        for key in listModel.keys():
            barangTrx = BarangTrx(barangTrx=listModel[key], qtyTrx=listQty[key], transaksi=trxModel)
            barangTrx.save()
        self.__keranjang.getModel().barangkeranjang_set.all().delete()
        return trx.getId()
    def getTransaksi(self, id):
        self.trxDBsync()
        return self.__listTransaksi[id]
    def getAllTransaksi(self):
        self.trxDBsync()
        return self.__listTransaksi
    def trxDBsync(self):
        for el in self.__kontributorModel.transaksimodel_set.all():
            self.__listTransaksi[el.id] = Transaksi(el)
    def pembayaran(self, idTrx):
        self.getTransaksi(idTrx).createPembayaran()
    def konfirmasiSampai(self, idTrx):
        self.getTransaksi(idTrx).ubahStatus("Selesai")

class Transaksi:
    def __init__(self, transaksiModel):
        self.__transaksiModel = transaksiModel
        self.__idTransaksi = transaksiModel.id
        self.__waktuDibuat = transaksiModel.waktuDibuat
        self.__status = transaksiModel.status
        self.__totalHarga = transaksiModel.totalHarga
        self.__metodePengiriman = transaksiModel.metodePengiriman
    def createPembayaran(self):
        pembayaran = PembayaranModel(totalPembayaran=self.__totalHarga, transaksi=self.__transaksiModel)
        pembayaran.save()
        self.ubahStatus("Menunggu Konfirmasi")
    def ubahStatus(self, statusBaru):
        self.__status = statusBaru
        self.__transaksiModel.status = statusBaru
        self.__transaksiModel.save()
    def inputPengiriman(self, ekspedisi, resi):
        pengirimanModel = PengirimanModel(namaEkspedisi=ekspedisi, nomorResi=resi, transaksi=self.__transaksiModel)
        pengirimanModel.save()
        pengiriman = InformasiPengiriman(ekspedisi, resi, pengirimanModel)
        self.ubahStatus("Sedang Dikirim")
    def getId(self):
        return self.__idTransaksi
    def getTotalHarga(self):
        return self.__totalHarga
    def getStatus(self):
        return self.__status
    def getMetodePengiriman(self):
        return self.__metodePengiriman
    def getTotalBarang(self):
        return self.__transaksiModel.barangtrx_set.all().count()
    def getListBarang(self):
        return self.__transaksiModel.barangtrx_set.all()
    def getTrxModel(self):
        return self.__transaksiModel

class InformasiPengiriman:
    def __init__(self, ekspedisi, resi, model):
        self.__pengirimanModel = model
        self.__ekspedisi = ekspedisi
        self.__resi = resi
    def getDetailsPengiriman(self):
        return (self.__ekspedisi, self.__resi)