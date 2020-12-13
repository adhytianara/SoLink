from django.urls import path
from .views import shoppage, checkout, riwayat

app_name = 'shop'

urlpatterns = [
    path('', shoppage, name='shoppage'),
    path('pembayaran/', checkout, name='checkout'),
    path('riwayat_transaksi/', riwayat, name='riwayat')
]