from django.db import models

# Create your models here.
class Std(models.Model):
    
    Student_name = models.CharField()
    Register_number= models.CharField()
    Department = models.CharField()
    Year = models.CharField()    
    Contact = models.CharField()
    Email_id =  models.EmailField()
    Transport =  models.CharField()
    Address = models.TextField()