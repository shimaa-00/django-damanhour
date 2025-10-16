from django.db import models

# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=20 ) # name(varchar(20))
    faculty = models.CharField (max_length=50)
    def __str__(self):
        return self.name
