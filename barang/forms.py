from django import forms
class TambahBarangForm(forms.Form):
    namaBarang = forms.CharField(max_length = 50)
    urlFoto = forms.CharField(max_length = 50)
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
    def __init__(self, *args, **kwargs):
        super(UpdateBarangForm, self).__init__(*args, **kwargs)
        self.fields['namaBarang'].initial = 'Collapsible Sillicone Cup'
        self.fields['urlFoto'].initial = 'https://zerowaste.id/wp-content/uploads/2020/06/IMG_0520-1.jpg'
        self.fields['hargaBarang'].initial = '225000'
        self.fields['jumlahStok'].initial = '55'
        self.fields['deskripsiBarang'].initial = 'Cup yang terbuat dari Plastik yang didaur ulang. Ukuran botol 400ml. Waktu kirim 2-5 hari kerja'