from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('transport/', Transport.as_view(), name='transport'),
    path('about/', About.as_view(), name='about'),
    path('category/<slug:slug>/', ProductsList.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
            ]