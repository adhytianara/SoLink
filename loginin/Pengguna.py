from .models import *
from barang.models import Barang

class Pengguna:
    def __init__(self, *args):
        self.__nama = args[0]
        self.__email = args[1]
        self.__username = args[2]
        self.__password = args[3]
        self.__noTelepon = args[4]
        self.__alamat = args[5]
    def melihatBarang(self):
        return Barang.objects.all()
    def getAlamat(self):
        return self.__alamat