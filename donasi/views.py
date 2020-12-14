from django.shortcuts import render

# Create your views here.
def donasipage(request):
    return render(request, 'donasipage.html', {})

def riwayatdonasi(request):
    return render(request, 'riwayatdonasi.html', {})

def formulirdonasi(request):
    return render(request, 'lembaga-sosial/ls-formulirdonasi.html', {})

def pembatalandonasi(request):
    return render(request, 'admin/admin-daftarPembatalanDonasi.html', {})