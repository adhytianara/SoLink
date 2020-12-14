from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.articleList, name='articleList'),
    path('viewArticle/', views.articleView, name='articleView'),
    path('createArticle/', views.createArticle, name='createArticle'),
    path('editArticle/', views.editArticle, name='editArticle'),
]