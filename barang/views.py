from django.shortcuts import render,redirect
from django.core import serializers
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from article.views import articleList
from loginin.Mitra import Mitra
from django.urls import reverse_lazy

# Create your views here.
def listBarang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Mitra":
            username = request.user.username
            mitra = Mitra(username)
            data = mitra.barangMitra()
            return render(request, 'barang.html',{'data':data})
    return HttpResponseRedirect(reverse_lazy('article:articleList'))

def tambahBarang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Mitra":
            if request.method == "POST":
                namaPemilik = request.user.username
                if Barang.objects.all().count() == 0:
                    idBarang = 1
                else :
                    idBarang = Barang.objects.order_by('-idBarang')[0].idBarang + 1
                namaBarang = request.POST['namaBarang']
                deskripsiBarang = request.POST['deskripsiBarang']
                urlFoto = request.POST['urlFoto']
                hargaBarang = request.POST['hargaBarang']
                jumlahStok = request.POST['jumlahStok']
                rating = 0
                stokRate = 0
                barang = Barang(namaPemilik=namaPemilik,idBarang=idBarang,namaBarang=namaBarang,deskripsiBarang=deskripsiBarang,
                urlFoto=urlFoto,hargaBarang=hargaBarang,jumlahStok=jumlahStok,rating=rating,stokRate=stokRate)
                mitra = Mitra(namaPemilik)
                mitra.menambahkanBarang(barang)
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