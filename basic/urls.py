from django.urls import path
from basic import views


app_name ='basic'

urlpatterns = [
    path('new', views.Make, name='urlshort.html'),
    path('<str:token>/', views.Home, name='urlshort.html'),
    
]
