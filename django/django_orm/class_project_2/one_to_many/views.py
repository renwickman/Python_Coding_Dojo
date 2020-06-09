from django.shortcuts import render, redirect
from .models import Teacher, Student

def index(request):
    context = {
        "all_teachers": Teacher.objects.all(),
        "all_students": Student.objects.all()
    }
    return render(request, "index.html", context)

def teacher(request):
    Teacher.objects.create(
        name=request.POST["teacher_name"], 
        age=request.POST["age"]
    )
    return redirect("/")

def student(request):
    Student.objects.create(
        name=request.POST["student_name"], 
        catchphrase=request.POST["catchphrase"],
        teacher=Teacher.objects.get(id=request.POST["teacher_name"])
    )
    return redirect("/")

def delete(request, id):
    if request.method == "POST":
        teacher_to_delete = Teacher.objects.get(id=id)
        teacher_to_delete.delete()
    return redirect("/")

# Create your views here.
