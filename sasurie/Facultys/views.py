from django.shortcuts import render
from .models import Faculty

# Create your views here.

def Facultys(request):
    selected_department = request.session.get('department', None)
    faculty = Faculty.objects.filter(Department=selected_department)   
    return render(request,'facultydetails.html',{'faculty':faculty})

