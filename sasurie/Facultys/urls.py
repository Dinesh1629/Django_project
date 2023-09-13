

from django.urls import path

from . import views
 
urlpatterns = [
    path('Facultys',views.Facultys,name='Facultys')
]