from django.shortcuts import render, redirect
from .models import TransaksiModel
from loginin.Mitra import Mitra

# Create your views here.
mitra = Mitra("namaMitra")
def penjualan(request):
    lst = TransaksiModel.objects.exclude(status='Menunggu Pembayaran')
    print(lst)
    listTransaksi = []
    for el in lst:
        id = el.id
        pembeli = el.kontributor.pengguna.username
        totalItem = el.barangtrx_set.all().count()
        totalBayar = el.pembayaranmodel.totalPembayaran
        status = el.status
        listTransaksi.append((id,pembeli, totalItem, totalBayar, status))
    return render(request, 'mitra/mtr_shop.html', {'listTrx':listTransaksi})

def pengiriman(request):
    return render(request, 'mitra/mtr_pengiriman.html', {})

def konfirmasiTransaksi(request, id):
    mitra.konfirmasiTransaksi(id)
    return redirect('/mitra/penjualan/')