from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.fnindex,name='index'),
    path('home', views.fnhome,name='home')
]