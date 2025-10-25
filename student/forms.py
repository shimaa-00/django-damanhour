from django import forms
class StudentForm(forms.Form):
    name = forms.CharField(label="Student Name",required=True  , max_length=10 , min_length=3 , widget=forms.TextInput(attrs={"placeholder" : "Input your name"}))
    faculty = forms.CharField(required=True , widget=forms.TextInput(attrs={"placeholder" : "Input your name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "pass" , "id" :"pass" }))
    age = forms.IntegerField()
    gpa = forms.DecimalField(max_digits=3 , decimal_places=2)
    gender = forms.ChoiceField(choices=[("m" , "male") , ("f" , "female")] , widget=forms.RadioSelect())
    succeded_or_not = forms.BooleanField (widget=forms.CheckboxInput())
    img = forms.FileField()
from .models import Student
class StudentModelForm (forms.ModelForm):
    class Meta :
        model = Student
        fields = '__all__'
        exclude = ['age']
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder" : "input your name"}),
            "gpa" : forms.NumberInput()
        }
        help_texts={
            "name" :"enter a valid name with at least 3 characters ",
            "gpa" : "1.5 or more"

        }
    def clean_name (self):
        name = self.cleaned_data.get("name")
        if len(name) >=3 :
            return name
        else :
            raise forms.ValidationError ("name must be at least 3 characters ")
    def clean_gpa(self):
        gpa = self.cleaned_data.get("gpa")
        if gpa >= 1.5:
            return gpa 
        else :
            raise forms.ValidationError("gpa must be more than 1.5")
    def clean (self):
        super().clean()
        faculty = self.cleaned_data.get("faculty")
        if faculty not in ["cs" , "applied arts"] :
            raise forms.ValidationError("you must be in cs or applied arts only ")
        else:
            return faculty

