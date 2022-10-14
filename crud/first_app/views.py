from django.shortcuts import render


# Create your views here.
def index(request):
    diction ={'title':"INDEX"}
    return render( request,'first_app/index.html',context=diction)


def studentForm(request):
    diction ={'title':"STUDENT_FORM"}
    return render( request,'first_app/student_form.html',context=diction)    