from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Student(models.Model):
    stu_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)


class Subject(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=20)
    sub_code = models.CharField(max_length=20)


class Marks(models.Model):
    sub_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    stu_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.IntegerField(null=True, blank=True)
