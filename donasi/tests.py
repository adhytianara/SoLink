from django.test import TestCase, Client
from donasi.models import LembagaSosialModel
from donasi.managerLembagaSosial import LembagaSosialManager
from donasi.models import DonasiModel
from donasi.managerDonasi import DonasiManager
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


class DonasiTest(TestCase):

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

        user = User.objects.create(username="AdhytiaKontri")
        user.set_password('kontri12345')
        user.save()
        user.profile.role = "Kontributor/Pembeli"
        user.save()
        user = authenticate(username="AdhytiaKontri",password='kontri12345')

        user = User.objects.create(username="AdhytiaAdmin")
        user.set_password('admin12345')
        user.save()
        user.profile.role = "Admin"
        user.save()
        user = authenticate(username="AdhytiaAdmin",password='admin12345')

        user = User.objects.create(username="AdhytiaLs")
        user.set_password('lss12345')
        user.save()
        user.profile.role = "Lembaga Sosial"
        user.save()
        user = authenticate(username="AdhytiaLs",password='lss12345')


    def testMelakukanDonasi(self):
        response = self.client.get('/donasi/')
        self.client.login(username="AdhytiaKontri",password="kontri12345")

        payload = {
            "idLs": 1,
            "namaDonatur": "Adhytia",
            "jenisBarang": "Pakaian",
            "metodePengiriman": "Antar Sendiri",
            "tanggalPengiriman": "14/12/2020",
            "alamatJemput": "",
        };
        
        self.assertEqual(DonasiModel.objects.all().count(),1)

        response = self.client.post('/donasi/',payload)
        self.assertEqual(response.status_code,200)
        
        self.assertEqual(DonasiModel.objects.all().count(),2)


    def testMelihatRiwayatDonasi(self):
        response = self.client.get('/donasi/riwayat-donasi/')
        self.client.login(username="AdhytiaKontri",password="kontri12345")
        response = self.client.get('/donasi/riwayat-donasi/')
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
        response = self.client.get('/donasi/riwayat-donasi/')
        self.client.login(username="AdhytiaKontri",password="kontri12345")

        payload = {
            "idDonasi": 1,
            "alasanPembatalan": "Berubah pikiran",
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = self.client.post('/donasi/riwayat-donasi/',payload)
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

        response = self.client.post('/donasi/create-lembaga-sosial/',payload)
        self.assertEqual(response.status_code,200)

        self.assertEqual(LembagaSosialModel.objects.all().count(),2)


    def testLembagaSosialSetujuiDonasi(self):
        response = self.client.get('/donasi/lembaga-sosial/formulir-donasi/')
        self.client.login(username="AdhytiaLs",password="lss12345")

        payload = {
            "idDonasi": 1,
            "status": "Menunggu pengiriman",
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = self.client.post('/donasi/lembaga-sosial/formulir-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu pengiriman")


    def testLembagaSosialTolakDonasi(self):
        response = self.client.get('/donasi/lembaga-sosial/formulir-donasi/')
        self.client.login(username="AdhytiaLs",password="lss12345")

        payload = {
            "idDonasi": 1,
            "status": "Ditolak",
            "alasanPenolakan": "Sedang tidak menerima bantuan"
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = self.client.post('/donasi/lembaga-sosial/formulir-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Ditolak")


    def testAdminValidasiPembatalanDonasi(self):
        response = self.client.get('/donasi/admin/pembatalan-donasi/')
        self.client.login(username="AdhytiaAdmin",password="admin12345")

        status = "Permohonan pembatalan donasi dari donatur telah ditolak karena alasan yang tidak valid. Harap tunggu respon dari lembaga sosial"
        payload = {
            "idDonasi": 1,
            "status": status,
            "alasanPembatalan": ""
        };

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, "Menunggu persetujuan lembaga sosial")

        response = self.client.post('/donasi/admin/pembatalan-donasi/',payload)
        self.assertEqual(response.status_code,200)

        for e in DonasiModel.objects.all():
            donasi = e

        self.assertEqual(donasi.status, status)  

    
    def testDeleteAllDonasi(self):
        self.assertEqual(DonasiModel.objects.all().count(),1)
        response = self.client.get('/donasi/delete-all/')
        self.assertEqual(DonasiModel.objects.all().count(),0)