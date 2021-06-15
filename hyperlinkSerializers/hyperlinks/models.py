from django.db import models


class SubjectList(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


class StudentInfo(models.Model):
    name = models.CharField(max_length=30)
    student_id = models.IntegerField()
    subject = models.ManyToManyField(SubjectList, related_name='subjectinfo')
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def subject_list(self):
        subjects = [i for i in self.subject.all()]
        return subjects