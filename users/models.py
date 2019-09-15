from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    roll_no = models.CharField(max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_no

# Create your models here.
