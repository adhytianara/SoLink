from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.articleList, name='articleList'),
    path('view/', views.articleView, name='articleView'),
    path('create/', views.createArticle, name='createArticle'),
    path('edit/', views.editArticle, name='editArticle'),
]