
from django.urls import path 
from student.views import *

urlpatterns = [
    path("hello" ,handle_hello_request ),
    path('hi', handle_hi_request),
    path ('student_index' , student_index , name='student_index'),
    path ('student_global' , student_global),
    path ('custom_page' , custom_page),
    # path ('' , students , name ="students"),
    path ('' , list_students.as_view() , name ="students"),
    path ('add' , add_student , name ="add_student"),
    # path ('formadd' , student_form_add , name ="student_form_add"),
    # path ('formadd' , add_student_from_modelform , name ="student_form_add"),
    path ('formadd' , StudentAdd.as_view() , name ="student_form_add"),
    # path ('show/<id>' , show_student , name = "student_details"),
    path ('show/<pk>' , student_details.as_view() , name = "student_details"),
    path ('delete/<id>' , delete_student , name = "student_delete"),
]
