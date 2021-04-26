from django.db import models
from django.urls import reverse

# Create your models here.

class payment(models.Model):
    receipt = models.IntegerField()
    Receipt_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField()
    choice=(
        ('Cash','Cash'),
        ('Cheque','Cheque')
    )
    payment_type = models.CharField(max_length=20,choices=choice)
    ch_no=models.IntegerField()
    Bank_Name = models.CharField(max_length=55)
    Branch_Name = models.CharField(max_length=55)
    admission=models.ForeignKey('admission.admission',on_delete=models.CASCADE,related_name='admission',default=1,blank=True)

    def __str__(self):
        return f"{self.admission}"


    def get_absolute_url(self):
        return reverse('payment-list')


class payment_info(models.Model):
    receipt = models.IntegerField()
    Receipt_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField()
    choice=(
        ('Cash','Cash'),
        ('Cheque','Cheque')
    )
    payment_type = models.CharField(max_length=20,choices=choice)
    ch_no=models.IntegerField(blank=True,null=True,default=0)
    Bank_Name = models.CharField(max_length=55,blank=True)
    Branch_Name = models.CharField(max_length=55,blank=True)
    admission=models.ForeignKey('admission.admission',on_delete=models.CASCADE,related_name='admission_info',default=1,blank=True)

    def __str__(self):
        return f"{self.admission}"


    def get_absolute_url(self):
        return reverse('payment-list')