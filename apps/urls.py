
from django.urls import path
from . import views
from .views import pastpaper, download_pdf

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.books, name='books'),
    path('gallery/', views.gallery, name='gallery'),  # URL for gallery
    path('pastpapers/', pastpaper, name='pastpaper'),
    path('download/<path:file_id>/', download_pdf, name='download_pdf'),


   
]

