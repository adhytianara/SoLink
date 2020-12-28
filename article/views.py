from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
import random


# Create your views here.
def halamanArtikel(request):
    artikel = Artikel.objects.all().order_by('-timestamp')
    args = {
		'artikel': artikel,
	}
    return render(request, 'halamanArtikel.html', args)

def melihatArtikel(request, idArtikel):
    artikel = Artikel.objects.filter(idArtikel=idArtikel)
    artikelRandomActive = Artikel.objects.all().order_by('?')[:1]
    artikelRandom = Artikel.objects.all().order_by('?')[:3]
    args = {
		'artikel': artikel,
        'artikelRandomActive' : artikelRandomActive,
        'artikelRandom' : artikelRandom
	}
    return render(request, 'melihatArtikel.html', args)

def membuatArtikel(request):
    if request.method == "POST":
        input = request.POST
        judulArtikel = input['judulArtikel']
        abstraksiArtikel = input['abstraksiArtikel']
        isiArtikel = input['isiArtikel']
        gambarThumbnail = request.FILES['gambarThumbnail']
        if Artikel.objects.all().count() == 0:
            idArtikel = 1
        else :
            idArtikel = Artikel.objects.order_by('-idArtikel')[0].idArtikel + 1
        try : 
            artikel = Artikel(judulArtikel=judulArtikel, abstraksiArtikel=abstraksiArtikel, isiArtikel=isiArtikel, idArtikel=idArtikel, gambarThumbnail=gambarThumbnail)
            artikel.save()
            message = 'Artikel dengan judul "' + judulArtikel + '" berhasil dibuat'
        except :
            message = "Gagal membuat Artikel"
        request.session['pesan'] = message
        return HttpResponseRedirect('/mengelolaArtikel/')
    form = membuatArtikelForm()
    args = {
		'form':form,
	}
    return render(request, 'membuatArtikel.html', args)

def mengelolaArtikel(request):
    artikel = Artikel.objects.all().order_by('-timestamp')
    message = ""
    try :
        message = request.session.get('pesan')
        del request.session['pesan']
    except :
        message = ""
    args = {
		'artikel': artikel,
        'message': message
	}
    return render(request, 'mengelolaArtikel.html', args)

def mengubahArtikel(request, idArtikel):
    artikelObj = Artikel.objects.filter(idArtikel=idArtikel)
    artikelGet = Artikel.objects.get(idArtikel=idArtikel)
    judulArtikelObj = artikelObj[0].judulArtikel
    abstraksiArtikelObj = artikelObj[0].abstraksiArtikel
    isiArtikelObj = artikelObj[0].isiArtikel
    gambarThumbnailObj = artikelObj[0].gambarThumbnail
    form = mengubahArtikelForm(initial={'idArtikel' : idArtikel, 'judulArtikel' : judulArtikelObj, 'abstraksiArtikel' : abstraksiArtikelObj, 'isiArtikel' : isiArtikelObj, 'gambarThumbnail' : gambarThumbnailObj})
    if request.method == "POST":
        input = request.POST
        judulArtikel = input['judulArtikel']
        abstraksiArtikel = input['abstraksiArtikel']
        isiArtikel = input['isiArtikel']
        try :
            gambarThumbnail = request.FILES['gambarThumbnail']
            artikelGet.gambarThumbnail.delete(save=True)
            artikelGet.setThumbnail(gambarThumbnail)
            artikelGet.save()
        except :
            pass
        try :
            artikelGet.setJudul(judulArtikel)
            artikelGet.setAbstraksi(abstraksiArtikel)
            artikelGet.setIsi(isiArtikel)
            message = 'Artikel dengan judul "' + judulArtikel + '" berhasil diubah'
        except :
            message = "Gagal mengubah Artikel"
        request.session['pesan'] = message
        return HttpResponseRedirect('/mengelolaArtikel/')
    args = {
		'form':form,
        'idArtikel':idArtikel
	}
    return render(request, 'mengubahArtikel.html', args)

def menghapusArtikel(request, idArtikel):
    try :
        artikelGet = Artikel.objects.get(idArtikel=idArtikel)
        message = 'Artikel dengan judul "' + artikelGet.judulArtikel + '" berhasil terhapus'
        artikelGet.gambarThumbnail.delete(save=True)
        artikelGet.delete()
    except Exception:
         message = "Gagal menghapus!!! Artikel tidak tersedia / sudah terhapus"
    request.session['pesan'] = message
    return HttpResponseRedirect('/mengelolaArtikel/')