from django.shortcuts import render

# Create your views here.
def penjualan(request):
    return render(request, 'mitra/mtr_shop.html', {})