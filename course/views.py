from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse ("<h1> Show Course </h1>")
def show_course(request , code):
    return HttpResponse (f"<h1> Course code {code} </h1>")
def course_name(request , name):
    return HttpResponse (f"<h1> Course name {name} </h1>")
