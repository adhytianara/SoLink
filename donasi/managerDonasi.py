from donasi.models import DonasiModel

class DonasiManager:
    __instance = None

    @staticmethod
    def getInstance():
        if DonasiManager.__instance == None:
            DonasiManager()
        return DonasiManager.__instance

    def __init__(self):
        if DonasiManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DonasiManager.__instance = self

    def saveNewDonasi(self,ls,status,alasanPembatalan,jenisBarang,
        metodePengiriman,tanggalPengiriman,alamatJemput,
        namaDonatur,tanggalDonasi):
        donasiModel = DonasiModel(lembagaSosial=ls,status=status,alasanPembatalan=alasanPembatalan,jenisBarang=jenisBarang,
        metodePengiriman=metodePengiriman,tanggalPengiriman=tanggalPengiriman,alamatJemput=alamatJemput,
        namaDonatur=namaDonatur,tanggalDonasi=tanggalDonasi)
        donasiModel.save()

    def getAllDonasi(self):
        return DonasiModel.objects.all()

    def cancelDonasi(self, idDonasi, status, alasanPembatalan):
        DonasiModel.objects.filter(id=idDonasi).update(status=status, alasanPembatalan=alasanPembatalan)
        
    def updateStatusDonasi(self, idDonasi, status):
        DonasiModel.objects.filter(id=idDonasi).update(status=status)