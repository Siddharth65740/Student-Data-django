from django.db import models
from django.urls import reverse

# Create your models here.

class inquiry(models.Model):
    inquiry=models.IntegerField(blank=True,null=True)
    date=models.DateField(null=True,blank=True)
    first_name=models.CharField(max_length=22,null=True,blank=True)
    second_name=models.CharField(max_length=22,null=True,blank=True)
    state_name=models.CharField(max_length=22,null=True,blank=True)
    area_name=models.CharField(max_length=22,null=True,blank=True)
    city_name=models.CharField(max_length=22,null=True,blank=True)
    mobile_num=models.IntegerField(null=True,blank=True,default=0)
    landline_num=models.IntegerField(null=True,blank=True,default=0)
    education=models.CharField(max_length=22,null=True,blank=True)
    clg_name=models.CharField(max_length=22,null=True,blank=True)
    course=models.ForeignKey('course.course_master',on_delete=models.CASCADE,related_name='inquiry',default=1,null=True,blank=True)
    ref_name=models.CharField(max_length=22,null=True,blank=True)
    remarks=models.CharField(max_length=22,null=True,blank=True)
    inq_held_by=models.CharField(max_length=22,null=True,blank=True)
    inq_num=models.IntegerField(null=True,blank=True,default=0)
    demo_lect_date=models.DateField(null=True,blank=True)
    demo_lect_time=models.TimeField(null=True,blank=True)


    def __str__(self):
        return f"{self.first_name}"

    def get_absolute_url(self):             # helps to redirect to another page
        return reverse('inquiry-list')