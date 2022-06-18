from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=70) 
    assignment = models.FileField(upload_to='pdfs/')
    date = models.DateField()
