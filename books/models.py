from django.db import models
import os
from pdf2jpg import pdf2jpg
# Create your models here.
BRANCH_CHOICES = (
    ('CSE','Computer Science Engineering'),
    ('ECE','Electronics & Communication Engineering'),
)

def get_file_path(instance, filename):
    upload_dir = os.path.join('media',instance.branch,str(instance.year))
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

class Book(models.Model):
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=15,choices=BRANCH_CHOICES,default='CSE')
    year = models.IntegerField()
    file = models.FileField(upload_to = get_file_path)
    def __str__(self):
        return self.name