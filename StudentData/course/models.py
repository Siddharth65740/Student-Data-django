from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class course_master(models.Model):
    name=models.CharField(max_length=45)
    description = models.TextField()
    duration = models.IntegerField()
    fees=models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Deactive', 'Deactive')])
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='course')

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):             # helps to redirect to another page
        return reverse('course-list')






