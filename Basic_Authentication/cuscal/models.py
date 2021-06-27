from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Subject(models.Model):
    course_name = models.CharField(max_length=50, blank=True, null=True)
    course_code = models.CharField(max_length=30, blank=True, null=True)
    active = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=True, blank=True, null=True)

    def __str__(self):
        return self.course_name


class Teacher(models.Model):
    class FacultyType(models.TextChoices):
        FULL_TIME = 'ft', _('Full-Time')
        PART_TIME = 'pt', _('Part-Time')

    teacher_name = models.CharField(max_length=30, blank=True, null=True)
    teacher_id = models.IntegerField(blank=True, null=True)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    type = models.CharField(max_length=10, choices=FacultyType.choices, default=FacultyType.FULL_TIME, blank=True,
                            null=True)
    subject_ids = models.ManyToManyField(Subject, blank=True, related_name='subject_teacher')
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.teacher_name

    @property
    def teacher_subject(self):
        teachers = [i for i in self.subject_ids.all()]
        return teachers


class Student(models.Model):
    student_name = models.CharField(max_length=30, blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    subject_ids = models.ManyToManyField(Subject, blank=True, related_name='subject_student')
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.student_name

    @property
    def subject_list(self):
        subjects = [i for i in self.subject_ids.all()]
        return subjects

    @property
    def teacher_list(self):
        teachers = [i for i in self.teacher_ids.all()]
        return teachers


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    teacher_ids = models.ForeignKey(Teacher, blank=True, on_delete=models.CASCADE, related_name='teacher_review')
    active = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.description
