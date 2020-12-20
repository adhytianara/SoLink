from django.urls import path
from .views import loginin,signup
#url for app

app_name = 'loginin'

urlpatterns = [
    path('', loginin,name ='loginin'),
    path('signup/', signup ,name ='signup'),
]