from django.shortcuts import render, redirect
from .models import Book, Author #need this to do ANYTHING with models

def index(request):
    context = {
        'all_books': Book.objects.all() #getting all Book dictionaries in DB and storing it in a dictionary called context
    }
    return render(request, 'index.html', context) #passing in the results of my query

def createBook(request): #nothing being passed into route/path, so only request goes in ()s
    if request.method == "POST": #if I'm not just typing in the route into my URL bar; if I didn't have this line and typed in the URL, anything with request.POST would error as it would be a GET request, meaning request.POST is non-existent
        Book.objects.create(title=request.POST['title'], description=request.POST['description']) #trusting all data given, no validations
    return redirect('/') #whether I make a Book or not, redirect me to the root page where I will be shown a template
def viewOneBook(request, id): #one thing is being passed in through route/path, called "id", therefore it needs to be added alongside request to what is being passed into this function
    context = {
        'book': Book.objects.get(id=id), #"id" on left side of = is the field I am searching for in DB, right side "id" is the variable I passed into this function
        'all_authors': Author.objects.all()
    }
    return render(request, "one_book.html", context)

def authorsIndex(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, "authors_index.html", context)

def createAuthor(request): #nothing being passed into route/path, so only request goes in ()s
    if request.method == "POST": #if I'm not just typing in the route into my URL bar; if I didn't have this line and typed in the URL, anything with request.POST would error as it would be a GET request, meaning request.POST is non-existent
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes']) #trusting all data given, no validations
    return redirect('/authorsIndex') #whether I make an Author or not, redirect me to the root page where I will be shown a template

def viewOneAuthor(request, id): #one thing is being passed in through route/path, called "id", therefore it needs to be added alongside request to what is being passed into this function
    context = {
        'author': Author.objects.get(id=id), #"id" on left side of = is the field I am searching for in DB, right side "id" is the variable I passed into this function
        'all_books': Book.objects.all()
    }
    return render(request, "one_author.html", context)

def addBook(request, id):
    this_author = Author.objects.get(id=id) #get Author from DB from route/path variable "id"
    this_book = Book.objects.get(id=request.POST['book_id']) #get Book from DB from key/value pair in request.POST
    this_author.books.add(this_book) #OR this_book.authors.add(this_author), either way creates the relationship
    return redirect(f'/authors/{id}') #using author's ID from route/path to redirect to same page we were just on
    #ALTERNATIVE: return redirect('/authors/'+str(id)) *Don't forget the str() if you do it this way! :)

def addAuthor(request, id):
    this_book = Book.objects.get(id=id) #get Book from DB from route/path variable "id"
    this_author = Author.objects.get(id=request.POST['author_id']) #get Author from DB from key/value pair in request.POST
    this_author.books.add(this_book) #OR this_book.authors.add(this_author), either way creates the relationship
    return redirect(f'/books/{id}') #using book's ID from route/path to redirect to same page we were just on
    #ALTERNATIVE: return redirect('/authors/'+str(id)) *Don't forget the str() if you do it this way! :)