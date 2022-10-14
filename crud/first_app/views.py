from django.shortcuts import render


# Create your views here.
def index(request):
    diction ={}
    return render( request,'first_app/index.html',context=diction)