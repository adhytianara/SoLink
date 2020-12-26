from django.test import TestCase, Client
from donasi.models import LembagaSosialModel
from donasi.managerLembagaSosial import LembagaSosialManager
from donasi.models import DonasiModel
from donasi.managerDonasi import DonasiManager
class DonasiKontributorTest(TestCase):

    def setUp(self):
        super().setUp()

        lsmodel = LembagaSosialModel(namaLs="namaLs", deskripsi="deskripsi", urlFoto="urlFoto", namaPimpinan="namaPimpinan", 
        jenis="jenis", kapasitas="kapasitas", 
        kebutuhan="kebutuhan", nomorTeleponLs="nomorTeleponLs", alamat="alamat")
        lsmodel.save()

        donasiModel = DonasiModel(lembagaSosial=lsmodel,status="Menunggu persetujuan lembaga sosial",alasanPembatalan="",jenisBarang="Pakaian",
        metodePengiriman="Antar Sendiri",tanggalPengiriman="14/12/2020",alamatJemput="",
        namaDonatur="Adhytia",tanggalDonasi="10/12/2020")
        donasiModel.save()


    def testMelakukanDonasi(self):
        payload = {
            "idLs": 1,
            "namaDonatur": "Adhytia",
            "jenisBarang": "Pakaian",
            "metodePengiriman": "Antar Sendiri",
            "tanggalPengiriman": "14/12/2020",
            "alamatJemput": "",
        };
        
        self.assertEqual(DonasiModel.objects.all().count(),1)

        response = Client().post('/donasi/',payload)
        self.assertEqual(response.status_code,200)
        
        self.assertEqual(DonasiModel.objects.all().count(),2)
