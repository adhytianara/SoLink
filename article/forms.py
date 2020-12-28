from django import forms

from ckeditor.widgets import CKEditorWidget

class membuatArtikelForm(forms.Form):
    judulArtikel = forms.CharField(label='Judul Artikel',max_length=50, widget=forms.TextInput(attrs={'placeholder':'Max : 50 char'}))
    abstraksiArtikel = forms.CharField(label='Abstraksi Singkat',max_length=360, widget=forms.Textarea(attrs={'rows': 8, 'placeholder':'Max : 360 char'}))
    isiArtikel = forms.CharField(label='Isi Artikel', widget=CKEditorWidget())
    gambarThumbnail = forms.ImageField(label='Gambar Thumbnail')
    def __init__(self, *args, **kwargs):
        super(membuatArtikelForm, self).__init__(*args, **kwargs)
        self.fields['judulArtikel'].widget.attrs['class'] = 'form-control'
        self.fields['abstraksiArtikel'].widget.attrs['class'] = 'form-control'
        self.fields['isiArtikel'].widget.attrs['class'] = 'form-control'
        

class mengubahArtikelForm(forms.Form):
    idArtikel = forms.IntegerField(label='ID Artikel', disabled = True)
    judulArtikel = forms.CharField(label='Judul Artikel',max_length=50, widget=forms.TextInput())
    abstraksiArtikel = forms.CharField(label='Abstraksi Singkat',max_length=360, widget=forms.Textarea(attrs={'rows': 8}))
    isiArtikel = forms.CharField(label='Isi Artikel', widget=CKEditorWidget())
    gambarThumbnail = forms.ImageField(label='Gambar Thumbnail')

    def __init__(self, *args, **kwargs):
        super(mengubahArtikelForm, self).__init__(*args, **kwargs)
        self.fields['judulArtikel'].widget.attrs['class'] = 'form-control'
        self.fields['abstraksiArtikel'].widget.attrs['class'] = 'form-control'
        self.fields['isiArtikel'].widget.attrs['class'] = 'form-control'