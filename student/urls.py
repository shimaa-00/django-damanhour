
from django.urls import path 
from student.views import *

urlpatterns = [
    path("hello" ,handle_hello_request ),
    path('hi', handle_hi_request),
    path ('student_index' , student_index , name='student_index'),
    path ('student_global' , student_global),
    path ('custom_page' , custom_page),
]
