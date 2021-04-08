from django.db import models
from django.contrib.auth.models import User
from PIL import  Image
from django.urls import reverse


# Create your models here.

class admission(models.Model):
    Student_Id=models.IntegerField()
    Date_of_addmission=models.DateField(null=True, blank=True)
    Course_Id=models.IntegerField()
    Addmission_Id=models.IntegerField()
    Start_Time=models.TimeField(auto_now=False, auto_now_add=False)
    End_Time=models.TimeField(auto_now=False, auto_now_add=False)
    Receipt_Id=models.IntegerField()
    Start_Date=models.DateField(null=True, blank=True)
    End_Date=models.DateField(null=True, blank=True)
    Fees=models.IntegerField()
    choice1=(
        ('Active','Active'),
        ('Deactive','Deactive')
    )
    Status=models.CharField(max_length=20,choices=choice1)
    No_of_Days=models.IntegerField()
    Remarks=models.CharField(max_length=22)
    choice = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    Pending_fees=models.CharField(max_length=20,choices=choice)

    def get_absolute_url(self):
        return reverse('admission-list')