from tkinter.tix import Form
from django import forms
from first_app import models

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = models.Student
        fields = '__all__'
        


