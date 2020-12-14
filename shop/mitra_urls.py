from django.urls import path
from .mitra_views import penjualan

app_name = 'shop'

urlpatterns = [
    path('penjualan/', penjualan, name='shoppage'),
]
