from django.urls import path

from . import views

urlpatterns = [
    path('Stud',views.Stud,name="Stud"),
    # path('landing',views.landing,name='landing')
]
