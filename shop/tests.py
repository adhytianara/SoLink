from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from barang.models import Barang
from.views import shoppage,deskripsi
# Create your tests here.
class ViewTest(TestCase):
    
    def setUp(self):
        super().setUp()
        user = User.objects.create(username="inisti")
        user.set_password('mitra123')
        user.save()
        user.profile.role = "Mitra"
        user.save()
        user = authenticate(username="inisti",password='mitra123')
        Barang.objects.create(namaPemilik="inisti",idBarang=100,namaBarang="buku aji",deskripsiBarang="Ini adalah buku aji",
                urlFoto="ajiinisti.com/buku.jpg",hargaBarang=50000,jumlahStok=30,rating=0,stokRate=0)

    def testUrlShopValid(self):
        self.client.login(username="inisti",password="mitra123")
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

    def testShopTemplate(self):
        self.client.login(username="inisti",password="mitra123")
        response = self.client.get('/shop/')
        self.assertTemplateUsed(response, 'shoppage.html')   
    
    def testShopView(self):
        response = resolve("/shop/")
        self.assertEqual(response.func,shoppage)
    
    def testShopBarang(self):
        response = self.client.get('/shop/')
        self.assertContains(response, 'buku aji')
        self.assertContains(response, '50000')