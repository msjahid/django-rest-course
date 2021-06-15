from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class FacultyType(models.TextChoices):
    FULL_TIME = 'ft', _('Full-Time')
    PART_TIME = 'pt', _('Part-Time')

class SubjectList(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


class StudentInfo(models.Model):
    student_name = models.CharField(max_length=30)
    student_id = models.IntegerField()
    subject = models.ManyToManyField(SubjectList, related_name='subjectinfo')
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

    @property
    def subject_list(self):
        subjects = [i for i in self.subject.all()]
        return subjects

class TeacherInfo(models.Model):
    teacher_name = models.CharField(max_length=30)
    teacher_id = models.IntegerField()
    type = models.CharField(max_length=10, choices=FacultyType.choices, default=FacultyType.FULL_TIME)
    course = models.ManyToManyField(SubjectList, related_name='courseinfo')
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    review_subject = models.ManyToManyField(TeacherInfo, related_name='reviewinfo')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
