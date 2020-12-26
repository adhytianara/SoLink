from django import forms
from donasi.models import LembagaSosialModel

class LembagaSosialForm(forms.ModelForm):
    class Meta:
        model = LembagaSosialModel
        fields = [
            "namaLs",
            "deskripsi",
            "urlFoto",
            "namaPimpinan",
            "jenis",
            "kapasitas",
            "kebutuhan",
            "nomorTeleponLs",
            "alamat"
        ]