from django.urls import path
from .views import donasipage, riwayatdonasi, formulirdonasi, pembatalandonasi

app_name = 'donasi'

urlpatterns = [
    path('', donasipage, name='donasipage'),
    path('riwayat-donasi/', riwayatdonasi, name='riwayatdonasi'),
    path('lembaga-sosial/formulir-donasi/', formulirdonasi, name='formulirdonasi'),
    path('admin/pembatalan-donasi/', pembatalandonasi, name='pembatalandonasi'),
]
