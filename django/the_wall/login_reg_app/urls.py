from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('wall', views.wall),
    path('post_comment', views.comment),
    path('post_message', views.message),
    path('delete_comment/<int:id>', views.deleteCom),
    path('delete_message/<int:id>', views.deleteMes),
    path('logout', views.logout)
]

