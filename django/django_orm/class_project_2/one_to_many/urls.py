from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('teacher', views.teacher),
    path('student', views.student),
    path('delete/<int:id>', views.delete)
]