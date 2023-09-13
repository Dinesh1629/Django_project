from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("landing",views.landing,name="landing"),
    path('process_form', views.process_form, name='process_form'),
    # path("studentsdetails",views.studentsdetails,name="studentsdetails"),
   
   
    ]