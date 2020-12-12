from django.shortcuts import render

# Create your views here.
def shoppage(request):
    return render(request, 'shoppage.html', {})

def checkout(request):
    return render(request, 'checkoutSuccess.html', {})

def riwayat(request):
    return render(request, 'riwayat.html', {})