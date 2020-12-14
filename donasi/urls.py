from django.urls import path
from .views import donasipage

app_name = 'donasi'

urlpatterns = [
    path('', donasipage, name='donasipage')
]
