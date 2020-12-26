from django.urls import path
from .views import *

app_name = 'donasi'

urlpatterns = [
    path('', donasipage, name='donasipage'),
    path('riwayat-donasi/', riwayatdonasi, name='riwayatdonasi'),
    path('lembaga-sosial/formulir-donasi/', formulirdonasi, name='formulirdonasi'),
    path('admin/pembatalan-donasi/', pembatalandonasi, name='pembatalandonasi'),
    path('create-lembaga-sosial/', createLembagaSosial, name='createLembagaSosial'),
]
