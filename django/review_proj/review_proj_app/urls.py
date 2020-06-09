from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('homepage', views.homepage),
    path('cats', views.createCat),
    path('vote/<int:id>', views.voteCat),
    path('unvote/<int:id>', views.unvoteCat),
    path('delete/<int:id>', views.deleteCat),
    path('profile', views.userProfile),
    path('cats/<int:id>', views.catProfile),
    path('logout', views.logout)
]