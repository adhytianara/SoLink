from django.contrib import admin
from .models import KontributorModel, KeranjangModel, BarangKeranjang, TransaksiModel, PembayaranModel, PengirimanModel, BarangTrx

# Register your models here.
admin.site.register(KontributorModel)
admin.site.register(KeranjangModel)
admin.site.register(BarangKeranjang)
admin.site.register(TransaksiModel)
admin.site.register(PembayaranModel)
admin.site.register(PengirimanModel)
admin.site.register(BarangTrx)
