from django.db import models
from django.contrib.auth.models import User
from PIL import  Image
from django.urls import reverse
# Create your models here.

class admission(models.Model):
    Student=models.ForeignKey('students.student',on_delete=models.CASCADE,related_name="admission",default=1,blank=True)
    Date_of_addmission=models.DateField(null=True, blank=True)
    Course=models.ForeignKey('course.course_master',on_delete=models.CASCADE,related_name="admission",default=1,blank=True)
    Start_Time=models.TimeField()
    End_Time=models.TimeField()
    Start_Date=models.DateField(null=True, blank=True)
    End_Date=models.DateField(null=True, blank=True)
    photo_copy=models.FileField(upload_to='media/',blank=True)
    Fees=models.IntegerField()
    choice1=(
        ('Active','Active'),
        ('Deactive','Deactive'),
        ('close','close')
    )
    Status=models.CharField(max_length=20,choices=choice1)
    No_of_Days=models.IntegerField()
    Remarks=models.CharField(max_length=22)
    Pending_fees=models.CharField(max_length=20)
    inquiry=models.ForeignKey('inquiry_table.inquiry',on_delete=models.CASCADE,related_name='admission',default=1)


    def __str__(self):
        return f"           {self.Student} - {self.Course} - {self.id}"

    def get_absolute_url(self):
        return reverse('admission-list')