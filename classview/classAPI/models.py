
from django.db import models


# Create your models here.


class StudentInfo(models.Model):
    name = models.CharField(max_length=20)
    studentId = models.IntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name