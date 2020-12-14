from django.urls import path
from .mitra_views import penjualan, pengiriman

app_name = 'mtr_shop'

urlpatterns = [
    path('penjualan/', penjualan, name='penjualan'),
    path('penjualan/input_pengiriman/', pengiriman, name='pengiriman')
]
