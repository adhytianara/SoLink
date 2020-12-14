from django.shortcuts import render

# Create your views here.
def donasipage(request):
    return render(request, 'donasipage.html', {})