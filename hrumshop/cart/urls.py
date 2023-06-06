from django.urls import path
from .views import *

urlpatterns = [
    path('', CartList.as_view(), name='cart'),
    path('order/', OrderAdd.as_view(), name='order_add'),
    path('order/accepted/', OrderAccepted.as_view(), name='order_accepted'),
    path('add/', cart_add, name='cart_add'),
    path('remove/', cart_remove, name='cart_remove'),
#     path('<int>:<id>/remove/',remove_in_cart , name='remove_in_cart'),
#     path('delete/', detele_in_cart, name='detele_in_cart'),
             ]

