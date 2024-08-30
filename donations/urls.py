from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('donations/', views.donations, name='donations'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
