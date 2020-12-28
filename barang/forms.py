from django import forms

class TambahBarangForm(forms.Form):
    namaBarang = forms.CharField(max_length = 50)
    urlFoto = forms.URLField(max_length=200)
    hargaBarang = forms.FloatField()
    jumlahStok = forms.IntegerField()
    deskripsiBarang = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super(TambahBarangForm, self).__init__(*args, **kwargs)
        self.fields['namaBarang'].widget.attrs['class'] = 'form-control'
        self.fields['urlFoto'].widget.attrs['class'] = 'form-control'
        self.fields['hargaBarang'].widget.attrs['class'] = 'form-control'
        self.fields['jumlahStok'].widget.attrs['class'] = 'form-control'
        self.fields['deskripsiBarang'].widget.attrs['class'] = 'form-control'
    
class UpdateBarangForm(TambahBarangForm):
    idBarang = forms.IntegerField(disabled = True)
    ratedStok = forms.IntegerField(disabled = True)
    rating = forms.FloatField(disabled = True)

    def __init__(self, *args, **kwargs):
        super(UpdateBarangForm, self).__init__(*args, **kwargs)
        self.fields['idBarang'].widget.attrs['class'] = 'form-control'
        self.fields['ratedStok'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['class'] = 'form-control'
        self.fields['idBarang'].initial = '0'
        self.fields['ratedStok'].initial = '0'
        self.fields['rating'].initial = '0'
        self.fields['namaBarang'].initial = 'Nama Barang'
        self.fields['urlFoto'].initial = 'Url Barang'
        self.fields['hargaBarang'].initial = '0'
        self.fields['jumlahStok'].initial = '0'
        self.fields['deskripsiBarang'].initial = 'Deskripsi Barang'

class HapusBarangForm(forms.Form):
    namaBarang = forms.CharField(max_length = 50, disabled = True)
    idBarang = forms.IntegerField(disabled = True)
    def __init__(self, *args, **kwargs):
        super(HapusBarangForm, self).__init__(*args, **kwargs)
        self.fields['idBarang'].initial = '0'
        self.fields['namaBarang'].initial = 'Nama Barang'
