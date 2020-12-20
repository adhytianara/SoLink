from django.shortcuts import render,redirect
from django.core import serializers
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from article.views import articleList
from django.urls import reverse_lazy
from barang.Mitra import Mitra

# Create your views here.
def listBarang(request):
    if request.user.is_authenticated:
    # print(request.user.profile.role == "Mitra")
        if request.user.profile.role == "Mitra":
            username = request.user.get_username()
            mitra = Mitra(username)
            data = mitra.barangMitra()
            return render(request, 'barang.html',{'data':data})
    # return render(request, 'barang.html', {})
    return HttpResponseRedirect(reverse_lazy('article:articleList'))

def tambahBarang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Mitra":
            if request.method == "POST":
                namaPemilik = request.user.username
                idBarang = Barang.objects.all().count() + 1
                namaBarang = request.POST['namaBarang']
                deskripsiBarang = request.POST['deskripsiBarang']
                urlFoto = request.POST['urlFoto']
                hargaBarang = request.POST['hargaBarang']
                jumlahStok = request.POST['jumlahStok']
                rating = 0
                stokRate = 0
                model = Barang(namaPemilik=namaPemilik,idBarang=idBarang,namaBarang=namaBarang,deskripsiBarang=deskripsiBarang,
                urlFoto=urlFoto,hargaBarang=hargaBarang,jumlahStok=jumlahStok,rating=rating,stokRate=stokRate)
                mitra = Mitra(namaPemilik)
                mitra.menambahkanBarang(model)
                return redirect('/barang/')
    form = TambahBarangForm()
    return render(request,'tambahBarang.html', {'form': form})

def konfirmasiUpdate(request,id):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.profile.role == "Mitra":
                idBarang = request.POST['idBarang']
                namaBarang = request.POST['namaBarang']
                deskripsiBarang = request.POST['deskripsiBarang']
                urlFoto = request.POST['urlFoto']
                hargaBarang = request.POST['hargaBarang']
                jumlahStok = request.POST['jumlahStok']
                # Barang.objects.select_related().filter(idBarang='idBarang').update(deskripsi=deskripsiBarang)
                Barang.objects.get(idBarang='idBarang').updateNama("AJI")
                data = Barang.objects.get(idBarang='idBarang')
                for blabla in data:
                    print(blabla.namaBarang)
                    print(blabla.deskripsiBarang)
                return redirect('/barang/')
    dataBarang = Barang.objects.all().filter(idBarang=id)
    form = UpdateBarangForm()
    for data in dataBarang:
        self.fields['idBarang'].initial = data.idBarang
        self.fields['ratedStok'].initial = data.stokRate
        self.fields['rating'].initial = data.rating
        self.fields['namaBarang'].initial = data.namaBarang
        self.fields['urlFoto'].initial = data.urlFoto
        self.fields['hargaBarang'].initial = data.hargaBarang
        self.fields['jumlahStok'].initial = data.jumlahStok
        self.fields['deskripsiBarang'].initial = data.deskripsiBarang
    return render(request, 'konfirmasiUpdate.html', {'form': form})

def updateBarang(request):
    return render(request, 'updateBarang.html', {})

def hapusBarang(request):
    return render(request, 'hapusBarang.html', {})

def konfirmasiHapus(request,id):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.profile.role == "Mitra":
                namaPemilik = request.user.username
                mitra = Mitra(namaPemilik)
                mitra.menghapusBarang(id)
                return redirect('/barang/')
    return HttpResponseRedirect(reverse_lazy('article:articleList'))