from django.db import models
from django.contrib.auth.models import User
from PIL import  Image
from django.urls import reverse


# Create your models here.

class admission(models.Model):
    Student_Id=models.IntegerField()
    Date_of_addmission=models.DateField()
    Course_Id=models.IntegerField()
    Addmission_Id=models.IntegerField()
    Start_Time=models.TimeField()
    End_Time=models.TimeField()
    Receipt_Id=models.IntegerField()
    Start_Date=models.DateField()
    End_Date=models.DateField()
    Fees=models.IntegerField()
    Status=models.CharField(max_length=6)
    No_of_Days=models.IntegerField()
    Remarks=models.CharField(max_length=22)
    Pending_fees=models.IntegerField()

    def __str__(self):
        return f"{self.Student_Id},{self.Date_of_addmission},{self.Course_Id},{self.Addmission_Id},{self.Start_Time}," \
               f"{self.End_Time},{self.Receipt_Id},{self.Start_Date},{self.End_Date}," \
               f"{self.Fees},{self.Status},{self.No_of_Days},{self.Remarks},{self.Pending_fees}"

    def get_absolute_url(self):
        return reverse('admission-list')