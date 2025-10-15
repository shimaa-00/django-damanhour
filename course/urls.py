from django.urls import path
from .views import show_course , courses , course_name
urlpatterns = [    
    # 127.0.0.1:8000/course
    path('' , courses),
    # 127.0.0.1:8000/course/show_course
    # path('show_course' , show_course),
    path('<int:code>' , show_course),
    path('<str:name>' , course_name),
]
