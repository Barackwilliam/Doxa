
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('paper/', views.pastpaper, name='pastpaper'),
    path('book/', views.books, name='books'),
    path('gallery/', views.gallery, name='gallery'),  # URL for gallery


   
]
