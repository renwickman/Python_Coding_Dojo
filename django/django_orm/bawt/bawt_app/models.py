from django.db import models

class Book(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    #"books" is now an attribute in the table Author as it is on the left side of the =
    #it refers to a list of Book dictionaries that are associated with a particular Author
    #EX: Author.objects.get(id=1).books.all()
    #
    #"authors" is now an attribute in the table Book as it is the related name associated with the table Book that is listed inside the ()s of the ManyToManyField
    #it refers to a list of Author dictionaries that are associated with a particular Book
    #EX: Book.objects.get(id=1).authors.all()
    #
    #this is the only relationship line I need as these are the only two tables (no Users, etc)
    #this was put in the Author table as it calls upon Book inside the ()s, can't reference Book if it hasn't been defined yet
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)