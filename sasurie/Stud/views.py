from django.shortcuts import render
from .models import Std

# Create your views here.

def Stud(request):
    selected_department = request.session.get('department', None)
    selected_year=request.session.get('year', None)
    student = Std.objects.filter(Department=selected_department , Year=selected_year)
    return render(request,'studentsdetails.html',{'student':student})

    
    
    
    