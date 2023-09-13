from django.db import models



# Create your models here.

class Faculty(models.Model):
    
    F_name = models.CharField()
    F_id = models.CharField()
    Department = models.CharField()
    Designation = models.CharField()
    Qualification = models.CharField()
    Experience =  models.PositiveIntegerField()
    Contact = models.CharField()
    Email_id =  models.EmailField()
    Address = models.TextField()
    
