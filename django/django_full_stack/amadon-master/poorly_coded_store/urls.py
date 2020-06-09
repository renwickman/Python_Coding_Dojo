from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('clear', views.clear)
]
