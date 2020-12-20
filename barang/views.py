from django.shortcuts import render,redirect
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from .forms import *
from .models import *

# Create your views here.
def listBarang(request):
    return render(request, 'barang.html', {})

def tambahBarang(request):
    if request.method == "POST":
        return redirect('/barang/')
    form = TambahBarangForm()
    return render(request,'tambahBarang.html', {'form': form})

def masukanBarang(request):
    idBarang = 1
    namaBarang = request.POST['nama']
    deskripsiBarang = request.POST['deskripsi']
    urlFoto = request.POST['url']
    hargaBarang = request.POST['harga']
    jumlahStok = request.POST['jumlah']
    rating = 0
    stokRate = 0
    model = BarangModel(idBarang=idBarang,namaBarang=namaBarang,deskripsiBarang=deskripsiBarang,
    urlFoto=urlFoto,hargaBarang=hargaBarang,jumlahStok=jumlahStok,rating=rating,stokRate=stokRate)
    model.save()

def konfirmasiUpdate(request):
    if request.method == "POST":
        return redirect('/barang/')
    form = UpdateBarangForm()
    return render(request, 'konfirmasiUpdate.html', {'form': form})

def updateBarang(request):
    return render(request, 'updateBarang.html', {})

def hapusBarang(request):
    if request.method == "POST":
        return redirect('/barang/')
    return render(request, 'hapusBarang.html', {})