from .models import *
from barang.models import Barang

class Pengguna:

    def melihatBarang(self):
        return Barang.objects.all()