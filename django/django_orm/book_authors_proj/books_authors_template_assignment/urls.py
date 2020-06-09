from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book', views.book),
    path('books/<int:id>', views.bookDisplay),
    path('authors/<int:book_id>/showAuthor', views.showAuthor),
    path('authors', views.index2),
    path('authorAction', views.authorAction),
    path('authors/<int:id>', views.authorDisplay),
    path('books/<int:author_id>/showBook', views.showBook)
]