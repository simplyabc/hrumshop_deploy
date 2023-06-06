from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('transport/', transport, name='transport'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<slug:slug>/', ProductsList.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
            ]