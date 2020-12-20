from django.urls import path
from .views import *

app_name = 'barang'

urlpatterns = [
    path('', listBarang, name='listBarang'),
    path('update_barang/', updateBarang, name='update'),
    path('konfirmasi_update/<id>/', konfirmasiUpdate, name='konfirmasiUpdate'),
    path('hapus_barang/', hapusBarang, name='hapus'),
    path('tambah_barang/', tambahBarang, name='tambah'),
]
