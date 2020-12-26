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


    def testMelihatRiwayatDonasi(self):
        response = Client().get('/donasi/riwayat-donasi/')
        self.assertEqual(response.status_code,200)


    def testGetIntanceManager(self):
        LembagaSosialManager.getInstance()
        try:
            LembagaSosialManager()
        except:
            print("This class is a singleton!")

        DonasiManager.getInstance()
        try:
            DonasiManager()
        except:
            print("This class is a singleton!")


    def testBatalkanDonasi(self):
        payload = {
            "idDonasi": 1,
            "alasanPembatalan": "Berubah pikiran",
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = Client().post('/donasi/riwayat-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Donatur mengajukan pembatalan. Sedang diproses admin")


    def testCreateLembagaSosial(self):
        payload = {
            "namaLs": "namaLs",
            "deskripsi": "deskripsi",
            "urlFoto": "urlFoto",
            "namaPimpinan": "namaPimpinan",
            "jenis": "jenis",
            "kapasitas": "kapasitas",
            "kebutuhan": "kebutuhan",
            "nomorTeleponLs": "nomorTeleponLs",
            "nomorTeleponLs": "nomorTeleponLs",
            "alamat": "alamat",
        };

        self.assertEqual(LembagaSosialModel.objects.all().count(),1)

        response = Client().post('/donasi/create-lembaga-sosial/',payload)
        self.assertEqual(response.status_code,200)

        self.assertEqual(LembagaSosialModel.objects.all().count(),2)


    def testLembagaSosialSetujuiDonasi(self):
        payload = {
            "idDonasi": 1,
            "status": "Menunggu pengiriman",
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = Client().post('/donasi/lembaga-sosial/formulir-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu pengiriman")


    def testLembagaSosialTolakDonasi(self):
        payload = {
            "idDonasi": 1,
            "status": "Ditolak",
            "alasanPenolakan": "Sedang tidak menerima bantuan"
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = Client().post('/donasi/lembaga-sosial/formulir-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Ditolak")


    def testAdminValidasiPembatalanDonasi(self):
        status = "Permohonan pembatalan donasi dari donatur telah ditolak karena alasan yang tidak valid. Harap tunggu respon dari lembaga sosial"
        payload = {
            "idDonasi": 1,
            "status": status,
            "alasanPembatalan": ""
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = Client().post('/donasi/admin/pembatalan-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, status)  