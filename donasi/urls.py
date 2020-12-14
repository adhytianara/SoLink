from django.urls import path
from .views import donasipage, riwayatdonasi, formulirdonasi

app_name = 'donasi'

urlpatterns = [
    path('', donasipage, name='donasipage'),
    path('riwayat-donasi/', riwayatdonasi, name='riwayatdonasi'),
    path('formulir-donasi/', formulirdonasi, name='formulirdonasi'),
    
]
