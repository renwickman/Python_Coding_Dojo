from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file

# When I make a new function in a path in my urls.py, I go to my views.py file to make that function immediately
urlpatterns = [
    path('', views.index),
    path('books', views.createBook),
    path('books/<int:id>', views.viewOneBook),
    path('authorsIndex', views.authorsIndex),
    path('authors', views.createAuthor),
    path('authors/<int:id>', views.viewOneAuthor),
    path('addBook/<int:id>', views.addBook),
    path('addAuthor/<int:id>', views.addAuthor),
]