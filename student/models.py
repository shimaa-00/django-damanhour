from django.db import models
from datetime import date
from django.utils import timezone
from course.models import Course
from track.models import Track
# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=20  , verbose_name="Student Name" ) # name(varchar(20))
    faculty = models.CharField (max_length=50)
    age = models.IntegerField (null = True , blank=True)
    gpa = models.DecimalField(max_digits=3 , decimal_places=2 , default=2.5 ) 
    gender = models.CharField (max_length=10 , choices=[("m" , "male") , ("f" , "female")]  , default='m')
    succeded_or_not = models.BooleanField (default=True)
    img = models.ImageField(upload_to='student/' , null = True , blank=True )
    birth_date = models.DateTimeField(null = True,default = timezone.datetime(2000 , 12 , 12) )
    date_joined = models.DateTimeField(auto_now_add=True , null=True)
    date_updated = models.DateTimeField(auto_now=True ,null = True)
    courses = models.ManyToManyField(Course)
    track = models.ForeignKey(Track , on_delete=models.PROTECT , null = True )
    def __str__(self):
        return self.name
