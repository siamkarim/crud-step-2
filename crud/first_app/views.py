from django.shortcuts import render
from first_app import forms

# Create your views here.
def index(request):
    diction ={'title':"INDEX"}
    return render( request,'first_app/index.html',context=diction)


def student_form(request):
    form = forms.StudentForm

    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction ={'title':"STUDENT_FORM",'student_form':form}
    return render( request,'first_app/student_form.html',context=diction)    