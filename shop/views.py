from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from loginin.Pengguna import Pengguna
from barang.models import Barang
from .models import KontributorModel, TransaksiModel, KeranjangModel
from .Kontributor import Kontributor
from django.http.response import JsonResponse
from loginin.Mitra import Mitra
from django.http import HttpResponse

# Create your views here.
pengguna = Pengguna("dummy", "dummy@dummy.com", "dummy", "dummy", "dummy", "dummy")
mitra = Mitra("namaMitra")
kontributorDict = {}

def getKontributor(uname):
    kontributorDBcount = KontributorModel.objects.all().count()
    if kontributorDBcount == len(kontributorDict):
        pass
    else:
        for el in KontributorModel.objects.all():
            kontributorDict[el.pengguna.username] = Kontributor(el, el.pengguna.username, el.pengguna.email, el.pengguna.username, el.pengguna.password, "08123456789", "Kampus Baru UI, Margonda Raya, Depok 12345")

    if uname in kontributorDict.keys():
        return kontributorDict[uname]
    else:
        penggunaModel = User.objects.get(username=uname)
        keranjang = KeranjangModel()
        keranjang.save()
        kontributorModel = KontributorModel(pengguna=penggunaModel, urlFotoDiriDenganKtp="urlFotoDiriDenganKtp", urlFotoKTP="urlFotoKTP", keranjang=keranjang)
        kontributorModel.save()
        kontributor = Kontributor(kontributorModel, penggunaModel.username, penggunaModel.email, penggunaModel.username, penggunaModel.password, "08123456789", "Kampus Baru UI, Margonda Raya, Depok 12345")
        kontributorDict[uname] = kontributor
        return kontributor

def shoppage(request):
    data = pengguna.melihatBarang()
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            mitra.setListTransaksi(kontributor.getAllTransaksi())
            return render(request, 'shoppage.html',{'data': data, 'keranjang': kontributor.getKeranjang()})
    return render(request, 'shoppage.html',{'data': data})

def checkout(request, id):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            trx = kontributor.getTransaksi(int(id))
            biaya = trx.getTotalHarga()
            return render(request, 'checkoutSuccess.html', {'biaya':biaya})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def riwayat(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            lst = kontributor.getAllTransaksi().values()
            listTransaksi = []
            for el in lst:
                id = el.getId()
                totalItem = el.getTotalBarang()
                totalHarga = el.getTotalHarga()
                status = el.getStatus()
                metodePengiriman = el.getMetodePengiriman()
                ekspedisi = ""
                resi = ""
                if status == 'Sedang Dikirim' or status == 'Selesai':
                    ekspedisi = el.getTrxModel().pengirimanmodel.namaEkspedisi
                    resi = el.getTrxModel().pengirimanmodel.nomorResi
                listTransaksi.append((id, totalItem, totalHarga, metodePengiriman, status, ekspedisi, resi))
            return render(request, 'riwayat.html', {'listTransaksi':listTransaksi})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def deskripsi(request,id):
    data = Barang.objects.get(idBarang=id)
    return render(request, 'deskripsiBarang.html',{'data':data})

@csrf_exempt
def tambahBarangKeranjang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            jsonRslt = {}
            if request.method == "POST":
                idBarang = request.POST["idBarang"]
                result = kontributor.tambahBarangKeranjang(idBarang)
                jsonRslt['nama'] = result
            return JsonResponse(jsonRslt)
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def keranjangModal(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            keranjang = kontributor.getKeranjang()
            listBarang = keranjang.getModel().barangkeranjang_set.all()
            jsonRslt = {}
            count = 0
            for el in listBarang:
                count +=1
                barangJson = {}
                barangJson['nama'] = el.barang.namaBarang
                barangJson['harga'] = el.barang.hargaBarang
                barangJson['id'] = el.id
                jsonRslt[count] = barangJson
            jsonRslt['count'] = count
            jsonRslt['total'] = keranjang.hitungTotal()
            return JsonResponse(jsonRslt)
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

@csrf_exempt
def hapusBarangKeranjang(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            if request.method == "POST":
                idBarang = request.POST["idBarang"]
                barangTrx = kontributor.getKeranjang().getModel().barangkeranjang_set.all().get(id=idBarang)
                barangTrx.delete()
            return JsonResponse({})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def checkoutModal(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            keranjang = kontributor.getKeranjang()
            listBarang = keranjang.getModel().barangkeranjang_set.all()
            jsonRslt = {}
            count = 0
            for el in listBarang:
                count +=1
                barangJson = {}
                barangJson['nama'] = el.barang.namaBarang
                barangJson['harga'] = el.barang.hargaBarang
                barangJson['id'] = el.id
                jsonRslt[count] = barangJson
            jsonRslt['count'] = count
            jsonRslt['total'] = keranjang.hitungTotal()
            jsonRslt['alamat'] = kontributor.getAlamat()
            return JsonResponse(jsonRslt)
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

@csrf_exempt
def createTrx(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            if request.method == "POST":
                totalHarga = request.POST['total']
                metode = request.POST['metode']
                trxId = kontributor.createTransaksi(totalHarga, metode, kontributor.getModel(), mitra)
            return JsonResponse({'id':trxId})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def riwayatModal(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            idTransaksi = request.GET['id']
            transaksi = kontributor.getTransaksi(int(idTransaksi))
            jsonRslt = {}
            count = 0
            ongkir = transaksi.getTotalHarga()
            for el in transaksi.getListBarang():
                count +=1
                barangJson = {}
                barangJson['nama'] = el.barangTrx.namaBarang
                barangJson['harga'] = el.barangTrx.hargaBarang
                barangJson['qty'] = el.qtyTrx
                barangJson['subtotal'] = el.subtotal()
                jsonRslt[count] = barangJson
                ongkir -= el.subtotal()
            jsonRslt['id'] = transaksi.getId()
            jsonRslt['status'] = transaksi.getStatus()
            jsonRslt['metode'] = transaksi.getMetodePengiriman()
            jsonRslt['ongkir'] = ongkir
            jsonRslt['count'] = count
            jsonRslt['total'] = transaksi.getTotalHarga()
            return JsonResponse(jsonRslt)
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def pembayaranTrx(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            idTransaksi = request.GET['id']
            kontributor.pembayaran(int(idTransaksi))
            jsonRslt = {'id':idTransaksi}
            return JsonResponse(jsonRslt)
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

def penjualan(request): 
    lst = TransaksiModel.objects.exclude(status='Menunggu Pembayaran')
    listTransaksi = []
    for el in lst:
        id = el.id
        pembeli = el.kontributor.pengguna.username
        totalItem = el.barangtrx_set.all().count()
        totalBayar = el.pembayaranmodel.totalPembayaran
        status = el.status
        listTransaksi.append((id,pembeli, totalItem, totalBayar, status))
    return render(request, 'mitra/mtr_shop.html', {'listTrx':listTransaksi})

def pengiriman(request, id):
    return render(request, 'mitra/mtr_pengiriman.html', {'id':id})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")

@csrf_exempt
def pengirimanDone(request):
    if request.method == "POST":
        idTrx = request.POST['id']
        ekspedisi = request.POST['ekspedisi']
        resi = request.POST['resi']
        trx = mitra.getTransaksi(int(idTrx))
        trx.inputPengiriman(ekspedisi, resi)
        return JsonResponse({})
    
def konfirmasiTransaksi(request, id):
    mitra.konfirmasiTransaksi(int(id))
    return redirect('/mitra/penjualan/')

def batalkanTransaksi(request, id):
    mitra.batalkanTransaksi(int(id))
    return redirect('/mitra/penjualan/')

def konfirmasiSampai(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            kontributor = getKontributor(request.user.username)
            idTrx = request.GET['id']
            kontributor.konfirmasiSampai(int(idTrx))
            return JsonResponse({'id':idTrx})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")
