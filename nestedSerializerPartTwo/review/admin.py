
from django.contrib import admin
from .models import StudentInfo, SubjectList, TeacherInfo

admin.site.register(SubjectList)

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):

    list_display = ['id', 'student_name', 'student_id', 'subject_list', 'address']

@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):

    list_display = ['id', 'teacher_name', 'teacher_id', 'type', 'course', 'contact']