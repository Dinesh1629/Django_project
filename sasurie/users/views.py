from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from Stud.models import Std
from Facultys.models import Faculty
from django.contrib.sessions.models import Session
from home.views import index

# Create your views here.

def login(request):
    # if 'username'  in request.session:
    #     return redirect(landing)
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        user = auth.authenticate(username=username,password=password)        
        if user is not None:
            request.session['username'] = username
            auth.login(request, user)
            uname= username
            print(uname)
            # return redirect(index)
            return render(request,'index.html',{'username':uname})
        
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html') 
    
# def index(request):
#     return render(request,'index.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('index')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
    
  
def logout(request):
     if 'username'  in request.session:
      request.session.flush()
     return redirect(login)



# def get_student():
#     cse_students = Std.objects.filter(Department='cse').count()
#     return cse_students

# def get_faculty():
#     row_count=Faculty.objects.count()
#     return row_count



def process_form(request):    
    if request.method == 'POST':
        selected_department = request.POST.get('department') # Get the selected department value
        selected_year = request.POST.get('year')
        
        students = Std.objects.filter(Department=selected_department, Year=selected_year).count()    
        # student_count = students.count()
        
        faculty = Faculty.objects.filter(Department=selected_department).count()    
        # faculty_count = faculty.count()
        total_strength = int(students) + int(faculty)
        return render(request, 'landing.html', {'total_strength':total_strength,'faculty': faculty,'students': students})
    
     


def landing(request):   
    student = get_student()   
    faculty = get_faculty()
    # total_strength = int(student) + int(faculty)
    # return render(request, 'landing.html', {'total_strength': total_strength,'faculty':faculty,'student':student})



