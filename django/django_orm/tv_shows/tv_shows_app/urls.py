from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.showIndex),
    path('shows/new', views.startShow),
    path('createShow', views.createShow),
    path('shows/<int:id>/redirect', views.submitEdit),
    path('shows/<int:id>/edit', views.editShow),
    path('shows/<int:id>', views.displayShow),
    path('shows/<int:id>/delete', views.deleteShow)
]
