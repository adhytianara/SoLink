from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.halamanArtikel, name='halamanArtikel'),
    path('melihatArtikel/<str:idArtikel>', views.melihatArtikel, name='melihatArtikel'),
    path('membuatArtikel/', views.membuatArtikel, name='membuatArtikel'),
    path('mengelolaArtikel/', views.mengelolaArtikel, name='mengelolaArtikel'),
    path('mengubahArtikel/<str:idArtikel>', views.mengubahArtikel, name='mengubahArtikel'),
    path('menghapusArtikel/<str:idArtikel>', views.menghapusArtikel, name='menghapusArtikel'),
]