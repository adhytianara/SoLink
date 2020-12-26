from .models import *
from barang.models import Barang

class Pengguna:

    def __init__(self,namaPemilik):
        self.namaPemilik = namaPemilik
    
    def melihatBarang(self):
        return Barang.objects.all()