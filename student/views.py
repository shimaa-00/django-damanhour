from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def handle_hello_request (request):
    response = HttpResponse ("<h1> Hello From Django </h1>")
    return response
def handle_hi_request(request):
    return HttpResponse("<h1>HI From Django</h1>")