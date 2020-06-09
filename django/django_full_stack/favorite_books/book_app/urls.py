from django.urls import path, views

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('logout', views.logout)
]