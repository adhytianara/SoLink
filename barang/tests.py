from django.test import TestCase, Client , RequestFactory
from django.urls import resolve
from .models import Barang
from loginin.models import Profile
from .forms import TambahBarangForm,UpdateBarangForm,HapusBarangForm
from .views import listBarang
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your tests here.
class BarangTest(TestCase):
    
    def setUp(self):
        super().setUp()
        Barang.objects.create(namaPemilik="inisti",idBarang=100,
            namaBarang="buku aji",deskripsiBarang="Ini adalah buku aji",
            urlFoto="ajiinisti.com/buku.jpg",hargaBarang=50000,jumlahStok=30,rating=0,stokRate=0)
    
    def testUpdateNama(self):
        data = Barang.objects.get(idBarang=100)
        data.updateNama("Aji")
        self.assertEqual(data.namaBarang,"Aji")
    
    def testUpdateDeskripsi(self):
        data = Barang.objects.get(idBarang=100)
        data.updateDeskripsi("Ini adalah deskripsi yang dites")
        self.assertEqual(data.deskripsiBarang,"Ini adalah deskripsi yang dites")
    
    def testUpdateHarga(self):
        data = Barang.objects.get(idBarang=100)
        data.updateHarga(23423)
        self.assertEqual(data.hargaBarang,23423)
    
    def testUpdateJumlahStok(self):
        data = Barang.objects.get(idBarang=100)
        data.updateJumlahStok(12)
        self.assertEqual(data.getJumlahStok(),12)

    def testUpdatePenilaian(self):
        data = Barang.objects.get(idBarang=100)
        data.tambahPenilaianRating(5)

        self.assertEqual(data.rating,5)
        data.tambahPenilaianRating(3)

        self.assertEqual(data.rating,4)
    
    def testUpdateFoto(self):
        data = Barang.objects.get(idBarang=100)
        data.updateFoto("ajiinisti2.com/buku.jpg")
        self.assertEqual(data.urlFoto,"ajiinisti2.com/buku.jpg")

class ViewTest(TestCase):
    
    def setUp(self):
        super().setUp()

        user = User.objects.create(username="inisti")
        user.set_password('mitra123')
        user.save()

        user.profile.role = "Mitra"
        user.save()
        user = authenticate(username="inisti",password='mitra123')
        
        Barang.objects.create(namaPemilik="inisti",
            idBarang=100,namaBarang="buku aji",deskripsiBarang="Ini adalah buku aji",
            urlFoto="ajiinisti.com/buku.jpg",hargaBarang=50000,jumlahStok=30,rating=0,stokRate=0)

    def testUrlKelolaBarangValid(self):
        self.client.login(username="inisti",password="mitra123")
        response = self.client.get('/barang/')
        self.assertEqual(response.status_code, 200)

    def testKelolaBarangTemplate(self):
        self.client.login(username="inisti",password="mitra123")
        response = self.client.get('/barang/')
        self.assertTemplateUsed(response, 'barang.html')   

    def testKelolaBarangRedirect(self):
        response = self.client.get('/barang/')
        self.assertEqual(response.status_code, 302)
    
    def testKelolaBarangView(self):
        response = resolve("/barang/")
        self.assertEqual(response.func,listBarang)