from django.db import models

# Create your models here.
class Student(models.Model):
	sid=models.IntegerField()
	sname=models.CharField(max_length=30)
	smail=models.EmailField(max_length=100)
	spass=models.CharField(max_length=20)
	sdept=models.CharField(max_length=10)