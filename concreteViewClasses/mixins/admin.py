from django.contrib import admin
from .models import Student, Subject, Teacher, Review

admin.site.register(Subject)


@admin.register(Student)
class StudentInfoAdmin(admin.ModelAdmin):

    list_display = ['student_id', 'student_name', 'subject_list', 'address']


@admin.register(Teacher)
class TeacherInfoAdmin(admin.ModelAdmin):

    list_display = ['teacher_id', 'teacher_name', 'type', 'teacher_subject', 'contact']


@admin.register(Review)
class ReviewInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'description', 'review_list', 'active', 'created']