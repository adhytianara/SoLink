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

def updateBarang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Mitra":
            username = request.user.username
            mitra = Mitra(username)
            data = mitra.barangMitra()
            return render(request, 'updateBarang.html',{'data':data})
    return HttpResponseRedirect(reverse_lazy('article:articleList'))

def konfirmasiUpdate(request,id):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.profile.role == "Mitra":
                namaBarang = request.POST['namaBarang']
                deskripsiBarang = request.POST['deskripsiBarang']
                urlFoto = request.POST['urlFoto']
                hargaBarang = request.POST['hargaBarang']
                jumlahStok = request.POST['jumlahStok']
                barang = Barang.objects.get(idBarang=id)
                barang.updateNama(namaBarang)
                barang.updateDeskripsi(deskripsiBarang)
                barang.updateFoto(urlFoto)
                barang.updateHarga(hargaBarang)
                barang.updateJumlahStok(jumlahStok)
                return redirect('/barang/')
    dataBarang = Barang.objects.all().filter(idBarang=id)
    form = UpdateBarangForm()
    for data in dataBarang:
        form.fields['idBarang'].initial = data.idBarang
        form.fields['ratedStok'].initial = data.stokRate
        form.fields['rating'].initial = data.rating
        form.fields['namaBarang'].initial = data.namaBarang
        form.fields['urlFoto'].initial = data.urlFoto
        form.fields['hargaBarang'].initial = data.hargaBarang
        form.fields['jumlahStok'].initial = data.jumlahStok
        form.fields['deskripsiBarang'].initial = data.deskripsiBarang
    return render(request, 'konfirmasiUpdate.html', {'form': form})

def hapusBarang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Mitra":
            username = request.user.username
            mitra = Mitra(username)
            data = mitra.barangMitra()
            return render(request, 'hapusBarang.html',{'data':data})
    return HttpResponseRedirect(reverse_lazy('article:articleList'))

def konfirmasiHapus(request,id):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.profile.role == "Mitra":
                namaPemilik = request.user.username
                mitra = Mitra(namaPemilik)
                mitra.menghapusBarang(id)
                return redirect('/barang/')
    dataBarang = Barang.objects.all().filter(idBarang=id)
    form = HapusBarangForm()
    for barang in dataBarang:
        form.fields['idBarang'].initial = barang.idBarang
        form.fields['namaBarang'].initial = barang.namaBarang
        foto = barang.urlFoto
    return render(request, "konfirmasiHapus.html",{'form':form,'image':foto})
