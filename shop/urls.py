from django.urls import path
from .views import shoppage, checkout, riwayat, deskripsi, tambahBarangKeranjang, keranjangModal, hapusBarangKeranjang, checkoutModal, createTrx, riwayatModal, pembayaranTrx, konfirmasiSampai

app_name = 'shop'

urlpatterns = [
    path('', shoppage, name='shoppage'),
    path('pembayaran/<id>', checkout, name='checkout'),
    path('riwayat_transaksi/', riwayat, name='riwayat'),
    path('deskripsi/<id>/', deskripsi, name='deskripsi'),
    path('tambah_barang_keranjang/', tambahBarangKeranjang, name='tambahBarangKeranjang'),
    path('modal_keranjang/', keranjangModal, name='keranjangModal'),
    path('modal_checkout/', checkoutModal, name='checkoutModal'),
    path('modal_riwayat/', riwayatModal, name='riwayatModal'),
    path('hapus_barang_keranjang/', hapusBarangKeranjang, name='hapusBarangKeranjang'),
    path('create_transaksi/', createTrx, name='createTrx'),
    path('pembayaran/', pembayaranTrx, name='pembayaran'),
    path('sampai/', konfirmasiSampai, name='pembayaran'),
]
