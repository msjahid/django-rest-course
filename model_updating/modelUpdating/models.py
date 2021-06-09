from django.db import models
from datetime import datetime
# Create your models here.

class SubjectList(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name

    @property
    def date(self):
        try:
            return self.created.strftime('%Y-%m-%d')
        except:
            return 'date is empty'

    @property
    def day(self):
        try:
            return self.created.strftime('%A')
        except:
            return 'day is empty'

    @property
    def month(self):
        try:
            return self.created.strftime('%B')
        except:
            return 'month is empty'

    @property
    def year(self):
        try:
            return self.created.strftime('%Y')
        except:
            return 'year is empty'

class StudentInfo(models.Model):
    name = models.CharField(max_length=30)
    student_id = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name