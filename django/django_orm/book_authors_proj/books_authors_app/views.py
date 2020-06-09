from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Authors

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "books.html", context)

def book(request):
    Book.objects.create(
        title=request.POST["title"],
        desc=request.POST["desc"]
    )
    return redirect("/")

def bookDisplay(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "authors": Book.objects.get(id=id).authors.all(),
        "all_authors": Authors.objects.all()
        }
    return render(request, "book_display.html", context)

def showAuthor(request, book_id):
    option = Authors.objects.get(id=request.POST['author_id'])
    book = Book.objects.get(id=book_id)
    book.authors.add(option)
    return redirect(f"/books/{book_id}")

def index2(request):
    context_3 = {
        "all_authors": Authors.objects.all()
    }
    return render(request, "authors.html", context_3)

def authorAction(request):
    Authors.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        notes=request.POST["notes"]
        )
    return redirect("/authors")

def authorDisplay(request, id):
    context = {
        "author": Authors.objects.get(id=id),
        "all_books": Book.objects.all()
    }
    return render(request, "authors_display.html", context)

def showBook(request, author_id):
    option = Book.objects.get(id=request.POST['book_id'])
    author = Authors.objects.get(id=author_id)
    author.books.add(option)  
    return redirect(f"/authors/{author_id}")

# Create your views here.
