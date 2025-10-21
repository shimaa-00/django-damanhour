from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def handle_hello_request (request):
    response = HttpResponse ("<h1> Hello From Django </h1>")
    return response
def handle_hi_request(request):
    return HttpResponse("<h1>HI From Django</h1>")
def student_index(request):
    dict = {"Name" : "Ahmed" , "Age" : 25}
    return render (request , "student/index.html" , dict )
def student_global (request):
    return render (request , 'student/student_global.html')
def custom_page(request):
    return render (request , "index.html")
def students(request):
    students = Student.objects.all()
    return render (request , 'student/students.html' , {"students" : students})