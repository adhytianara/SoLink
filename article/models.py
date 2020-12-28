from django.db import models
from datetime import datetime

from ckeditor.fields import RichTextField

# Create your models here.
class Artikel(models.Model):
    judulArtikel = models.CharField(max_length=50)
    abstraksiArtikel = models.TextField(max_length=360)
    isiArtikel = RichTextField(blank=True, null=True)
    idArtikel = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(default=datetime.now)
    gambarThumbnail = models.ImageField(upload_to = 'thumbnail_folder/', default = 'thumbnail_folder/None/no-img.jpg')

    def __str__(self):
        return self.judulArtikel

    def setJudul(self,judul):
        self.judulArtikel = judul
        self.save()

    def setAbstraksi(self,abstraksi):
        self.abstraksiArtikel = abstraksi
        self.save()

    def setIsi(self,isi):
        self.isiArtikel = isi
        self.save()

    def setThumbnail(self,gambar):
        self.gambarThumbnail = gambar
        self.save()
    
