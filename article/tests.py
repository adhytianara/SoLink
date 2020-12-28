from django.test import TestCase
from django.urls import resolve
from .models import Artikel
from loginin.models import Profile
from .forms import *
from .views import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your tests here.
class BarangTest(TestCase):
    
    def setUp(self):
        super().setUp()
        Artikel.objects.create(judulArtikel="Judul Test", abstraksiArtikel="Abstraksi test", 
            isiArtikel="Isi test", idArtikel=10, gambarThumbnail="thumbnail_folder/ihsan.jpg")
    
    def testSetJudul(self):
        data = Artikel.objects.get(judulArtikel="Judul Test")
        data.setJudul("Judul Baru")
        self.assertEqual(data.judulArtikel,"Judul Baru")

    def testSetAbstraksi(self):
        data = Artikel.objects.get(abstraksiArtikel="Abstraksi test")
        data.setAbstraksi("Abstraksi baru")
        self.assertEqual(data.abstraksiArtikel,"Abstraksi baru")
    
    def testSetIsi(self):
        data = Artikel.objects.get(isiArtikel="Isi test")
        data.setIsi("isi baru")
        self.assertEqual(data.isiArtikel,"isi baru")

    def testSetThumbnail(self):
        data = Artikel.objects.get(gambarThumbnail="thumbnail_folder/ihsan.jpg")
        data.setThumbnail("thumbnail_folder/baru.jpg")
        self.assertEqual(data.gambarThumbnail,"thumbnail_folder/baru.jpg")

class ViewTest(TestCase):
    def setUp(self):
        super().setUp()

        user = User.objects.create(username="ihsanAzizi")
        user.set_password('admin123')
        user.save()

        user.profile.role = "Admin"
        user.save()
        user = authenticate(username="ihsanAzizi",password='admin123')
        
        Artikel.objects.create(judulArtikel="Judul Test", abstraksiArtikel="Abstraksi test", 
            isiArtikel="Isi test", idArtikel=10, gambarThumbnail="thumbnail_folder/ihsan.jpg")
        
    def testUrlNotExist(self):
        response = self.client.get('/blank')
        self.assertEqual(response.status_code, 404)
    
    def testUrlHalamanArtikelValid(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testUrlHalamanArtikelTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'halamanArtikel.html')

    def testHalamanArtikelView(self):
        response = resolve("/")
        self.assertEqual(response.func,halamanArtikel)

    def testUrlMelihatArtikelValid(self):
        response = self.client.get('/melihatArtikel/10')
        self.assertEqual(response.status_code, 200)

    def testUrlMelihatArtikelTemplate(self):
        response = self.client.get('/melihatArtikel/10')
        self.assertTemplateUsed(response, 'melihatArtikel.html')
    
    def testUrlMembuatArtikelValid(self):
        self.client.login(username="ihsanAzizi",password="admin123")
        response = self.client.get('/membuatArtikel/')
        self.assertEqual(response.status_code, 200)

    def testUrlMembuatArtikelTemplate(self):
        self.client.login(username="ihsanAzizi",password="admin123")
        response = self.client.get('/membuatArtikel/')
        self.assertTemplateUsed(response, 'membuatArtikel.html')

    def testUrlMengelolaArtikelValid(self):
        self.client.login(username="ihsanAzizi",password="admin123")
        response = self.client.get('/mengelolaArtikel/')
        self.assertEqual(response.status_code, 200)
        
    def testUrlMengelolaArtikelTemplate(self):
        self.client.login(username="ihsanAzizi",password="admin123")
        response = self.client.get('/mengelolaArtikel/')
        self.assertTemplateUsed(response, 'mengelolaArtikel.html')

    def testUrlMengubahArtikelValid(self):
        self.client.login(username="ihsanAzizi",password="admin123")
        response = self.client.get('/mengubahArtikel/10')
        self.assertEqual(response.status_code, 200)

    def testUrlMengubahArtikelTemplate(self):
        self.client.login(username="ihsanAzizi",password="admin123")
        response = self.client.get('/mengubahArtikel/10')
        self.assertTemplateUsed(response, 'mengubahArtikel.html')
    
    # def testTambahArtikel(self):
    #     self.assertEqual(Artikel.objects.all().count(),1)

    #     self.client.login(username="ihsanAzizi",password="admin123")
    #     data = {
    #         "judulArtikel":"Judul Tambah",
    #         "abstraksiArtikel":"Abstraksi tambah",
    #         "isiArtikel":"Isi tambah",
    #         "gambarThumbnail": ""
    #     }
        
    #     response = self.client.post("/membuatArtikel/",data)
    #     self.assertEqual(response.status_code,302)
    #     self.assertEqual(Artikel.objects.all().count(),2)

    def testHapusArtikel(self):
        self.assertEqual(Artikel.objects.all().count(),1)

        self.client.login(username="ihsanAzizi",password="admin123")

        data = Artikel.objects.get(idArtikel=10)
        data.delete()

        self.assertEqual(Artikel.objects.all().count(),0)