from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Leave(models.Model):
    description=models.CharField(max_length=5000,default=0)
    start_date=models.DateField()
    end_data=models.DateField()
    total_days=models.CharField(max_length=100,default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # description start_date end_data total_days user