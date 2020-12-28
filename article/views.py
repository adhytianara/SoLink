from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from loginin.AdminClass import Admin
from .forms import *
from .models import *


# Create your views here.
def halamanArtikel(request):
    artikel = Artikel.objects.all().order_by('-timestamp')
    args = {
        'artikel': artikel,
    }
    return render(request, 'halamanArtikel.html', args)

def melihatArtikel(request, idArtikel):
    message = ""
    artikel = ""
    try :
        artikel = Artikel.objects.filter(idArtikel=idArtikel)
    except :
        message = "Gagal menampilkan artikel"
    args = {
        'artikel': artikel,
        'message': message
    }
    return render(request, 'melihatArtikel.html', args)

def membuatArtikel(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Admin":
            username = request.user.username
            admin = Admin(username)
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
                    admin.membuatArtikel(artikel)
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
    return HttpResponseRedirect(reverse_lazy('article:halamanArtikel'))

def mengelolaArtikel(request):
    if request.user.is_authenticated:
        if request.user.profile.role == "Admin":
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
    return HttpResponseRedirect(reverse_lazy('article:halamanArtikel'))

def mengubahArtikel(request, idArtikel):
    if request.user.is_authenticated:
        if request.user.profile.role == "Admin":
            username = request.user.username
            admin = Admin(username)
            artikelObj = Artikel.objects.filter(idArtikel=idArtikel)
            artikelGet = admin.getArtikel(idArtikel)
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
                except :
                    pass
                try :
                    admin.mengubahArtikel(idArtikel, judulArtikel, abstraksiArtikel, isiArtikel)
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
    return HttpResponseRedirect(reverse_lazy('article:halamanArtikel'))

def menghapusArtikel(request, idArtikel):
    if request.user.is_authenticated:
        if request.user.profile.role == "Admin":
            username = request.user.username
            admin = Admin(username)
            try :
                artikelGet = admin.getArtikel(idArtikel)
                message = 'Artikel dengan judul "' + artikelGet.judulArtikel + '" berhasil terhapus'
                admin.menghapusArtikel(idArtikel)
            except Exception:
                message = "Gagal menghapus!!! Artikel tidak tersedia / sudah terhapus"
            request.session['pesan'] = message
            return HttpResponseRedirect('/mengelolaArtikel/')
    return HttpResponseRedirect(reverse_lazy('article:halamanArtikel'))
    