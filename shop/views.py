from django.shortcuts import render
from loginin.Pengguna import Pengguna
from barang.models import Barang
# Create your views here.
pengguna = Pengguna()

def shoppage(request):
    data = pengguna.melihatBarang()
    return render(request, 'shoppage.html',{'data': data})

def checkout(request):
    return render(request, 'checkoutSuccess.html', {})

def riwayat(request):
    return render(request, 'riwayat.html', {})

def deskripsi(request):
    return render(request, 'deskripsiBarang.html', {})