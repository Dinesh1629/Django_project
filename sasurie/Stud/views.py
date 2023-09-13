from django.shortcuts import render
from .models import Std

# Create your views here.

def Stud(request):
  
    student = Std.objects.filter(Department='cse')
    return render(request,'studentsdetails.html',{'student':student})

    
    
    
    