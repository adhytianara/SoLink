from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from donasi.managerLembagaSosial import LembagaSosialManager
from donasi.managerDonasi import DonasiManager
from .createLSforms import LembagaSosialForm
from datetime import date


@csrf_exempt
def donasipage(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            lsManager = LembagaSosialManager.getInstance()
            donasiManager = DonasiManager.getInstance()
            if request.method == "POST":
                today = date.today()

                idLs = request.POST['idLs']
                namaDonatur = request.POST['namaDonatur']
                jenisBarang = request.POST['jenisBarang']
                metodePengiriman = request.POST['metodePengiriman']
                tanggalPengiriman = request.POST['tanggalPengiriman']
                alamatJemput = request.POST['alamatJemput']

                tanggalDonasi = today.strftime("%d/%m/%Y")
                status = "Menunggu persetujuan lembaga sosial"
                alasanPembatalan = ""
                ls = lsManager.getById(idLs)
            
                donasiManager.saveNewDonasi(ls,status,alasanPembatalan,jenisBarang,
                metodePengiriman,tanggalPengiriman,alamatJemput,
                namaDonatur,tanggalDonasi)

            data = lsManager.getAllLembagaSosial()
            return render(request, 'kontributor-melakukan-donasi/donasipage.html', {'data': data})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")


@csrf_exempt
def riwayatdonasi(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Kontributor/Pembeli":
            donasi = DonasiManager.getInstance()
            if request.method == "POST":
                idDonasi = request.POST['idDonasi']
                alasanPembatalan = request.POST['alasanPembatalan']

                status = "Donatur mengajukan pembatalan. Sedang diproses admin"
                donasi.cancelDonasi(idDonasi, status, alasanPembatalan)

            data = donasi.getAllDonasi()
            return render(request, 'kontributor-melihat-riwayat-donasi/riwayatdonasi.html', {'data': data})
    return HttpResponse("Kamu harus masuk sebagai <b>Kontributor/Pembeli</b> untuk melihat halaman ini")


@csrf_exempt
def formulirdonasi(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Lembaga Sosial":
            donasi = DonasiManager.getInstance()
            if request.method == "POST":
                idDonasi = request.POST['idDonasi']
                status = request.POST['status']

                if status == "Ditolak":
                    alasanPembatalan = request.POST['alasanPenolakan']
                    donasi.cancelDonasi(idDonasi, status, alasanPembatalan)
                else:
                    donasi.updateStatusDonasi(idDonasi, status)

            data = donasi.getAllDonasi()
            return render(request, 'lembaga-sosial/ls-formulirdonasi.html', {'data': data})
    return HttpResponse("Kamu harus masuk sebagai <b>Lembaga Sosial</b> untuk melihat halaman ini")    
    

@csrf_exempt
def adminDaftarPembatalandonasi(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Admin":
            donasi = DonasiManager.getInstance()
            if request.method == "POST":
                idDonasi = request.POST['idDonasi']
                status = request.POST['status']

                donasi.cancelDonasi(idDonasi, status, "")

            status = "Donatur mengajukan pembatalan. Sedang diproses admin"
            data = donasi.getDonasibyStatus(status)
            return render(request, 'admin/admin-daftarPembatalanDonasi.html', {'data': data})
    return HttpResponse("Kamu harus masuk sebagai <b>Admin</b> untuk melihat halaman ini")    
    

def createLembagaSosial(request):
    form = LembagaSosialForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LembagaSosialForm()

    context = {
        'form': form
    }
    return render(request, 'lembaga-sosial/createLembagaSosial.html', context)


def deleteAllDonasi(request):
    donasiManager = DonasiManager.getInstance()
    donasiManager.deleteAllDonasi()
    return redirect('/donasi/')
