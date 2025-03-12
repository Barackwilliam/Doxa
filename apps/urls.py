
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('female/', views.female, name='female'),
    path('male/', views.male, name='male'),
    path('child/', views.child, name='child'),
    path('electronic/', views.electronic, name='electronic'),
    path('handbag/', views.handbag, name='handbag'),  # URL for gallery
    path('shoes/', views.shoes, name='shoes'),
    path('contact/', views.contact, name='contact'),


   
]

