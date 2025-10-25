from django.shortcuts import render , get_object_or_404 , redirect
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
def students(request , context = {}):
    print (request.POST)
    students = Student.objects.all()
    context ["students"] = students
    return render (request , 'student/students.html' , context)
def show_student(request , id ):
    # student = Student.objects.get (pk = id)
    student = get_object_or_404(Student , pk=id)
    return render (request , 'student/showdetails.html' , {"student":student})
def delete_student(request , id):
    # student = get_object_or_404(Student , pk = id)
    try :
        student = Student.objects.get(pk = id).delete()
        return redirect ("students")
    except :
        context = {"error" : "student not found "}
        return students(request , context )
def add_student (request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        gpa = request.POST['gba']
        gender = request.POST["gender"]
        status = request.POST["status"]
        img = request.FILES['image']
        faculty = request.POST['faculty']
        context= {"errors" : []}
        new_student = Student()
        if len(name) >= 3:
            new_student.name = name
        else :
            context ["errors"].append("name must be at least 3 characters ")
            return render (request , 'student/add_student.html' , context)
        if int(age) >= 18 :
            new_student.age = age
        else :
            context["errors"].append("age must be +18")
            return render (request , 'student/add_student.html' , context)
        new_student.gpa = gpa 
        new_student.faculty = faculty
        new_student.gender = gender 
        new_student.susucceded_or_not = status
        new_student.img = img
        new_student.save()
        return redirect ("students")
    elif request.method == "GET":
        return render (request , 'student/add_student.html' )


from .forms import StudentForm
def student_form_add (request):
    if request.method == "GET":
        form = StudentForm()
        return render (request ,'student/formadd.html' , {"form" :form})
    elif request.method == "POST" :
        form = StudentForm(request.POST , request.FILES)
        print('errors : ' , form.errors)
        if form.is_valid():
            print("form valid")
            new_student = Student()
            new_student.name =  form.cleaned_data.get("name")
            new_student.age = form.cleaned_data["age"]
            new_student.gpa = form.cleaned_data["gpa"]
            new_student.img = form.cleaned_data["img"]
            new_student.faculty = form.cleaned_data["faculty"]
            new_student.gender = form.cleaned_data["gender"]
            new_student.save()
            print("object saved")
        return redirect("students")

        # return redirect ("students")



from .forms import StudentModelForm
def add_student_from_modelform(request):
    if request.method == "GET":
        form = StudentModelForm()
        return render (request , 'student/formadd.html' , {"form":form})
    elif request.method == "POST":
        form = StudentModelForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("students")
        else :
            return render (request , 'student/formadd.html' , {"form":form})
from django.views import View

class StudentAdd(View):
    def get(self, request):
        form = StudentModelForm()
        return render (request , 'student/formadd.html' , {"form":form})
    def post(self , request):
        form = StudentModelForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect ("students")
        else :
            return render (request , 'student/formadd.html' , {"form":form})




from django.views.generic import ListView , DetailView , DeleteView , CreateView , UpdateView
class list_students (ListView):
    model = Student
    template_name = "student/students.html"
    context_object_name = "students"


class student_details (DetailView):
    model = Student
    template_name = 'student/showdetails.html'
    context_object_name = "student"