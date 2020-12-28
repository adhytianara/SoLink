from .models import *
from article.models import Artikel

class Admin:

    def __init__(self,nama):
        self.nama = nama
        self.id = 0

    def membuatArtikel(self,artikelBaru):
        artikelBaru.save()

    def menghapusArtikel(self,_id):
        a = Artikel.objects.get(idArtikel=_id)
        a.gambarThumbnail.delete(save=True)
        a.delete()

    def mengubahArtikel(self, _id, judul, abstraksi, isi):
        a = Artikel.objects.get(idArtikel=_id)
        a.setJudul(judul)
        a.setAbstraksi(abstraksi)
        a.setIsi(isi)


    def getArtikel(self,_id):
        return Artikel.objects.get(idArtikel=_id)


