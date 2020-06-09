from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #render index.html
    path('owners', views.createOwner), #handles form data to make Owner, redirect
    path('success', views.success) #render success.html
]