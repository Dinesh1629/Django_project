from django.shortcuts import render
from .models import Faculty


# Create your views here.

def Facultys(request):
    faculty = Faculty.objects.filter(Department='cse')
   
    
    return render(request,'facultydetails.html',{'faculty':faculty})

