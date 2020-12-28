from django.urls import path
from .views import penjualan, pengiriman, konfirmasiTransaksi, pengirimanDone, riwayatModal, batalkanTransaksi

app_name = 'mtr_shop'

urlpatterns = [
    path('penjualan/', penjualan, name='penjualan'),
    path('penjualan/konfirmasi/<id>', konfirmasiTransaksi, name='konfirmasiTransaksi'),
    path('penjualan/batalkan/<id>', batalkanTransaksi, name='batalkanTransaksi'),
    path('penjualan/input_pengiriman/<id>', pengiriman, name='pengiriman'),
    path('penjualan/input_pengiriman/done/', pengirimanDone, name='pengirimanDone'),
    path('penjualan/modal_riwayat/', riwayatModal, name='riwayatModal'),
]
