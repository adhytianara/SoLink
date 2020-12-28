from .models import *
from article.models import Artikel

class Admin:

    def __init__(self,nama):
        self.nama = nama
        self.id = 0

    def membuatArtikel(self,artikelBaru):
        artikelBaru.save()

    def menghapusArtikel(self,id):
        a = Artikel.objects.get(idArtikel=id)
        a.delete()

    def getArtikel(self,id):
        return Artikel.objects.get(idArtikel=id)


