from django.db import models
from django.contrib import admin
class Student (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    collage=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    email=models.EmailField()


class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','collage','department','email')    

