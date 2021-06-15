from django.contrib import admin
from .models import StudentInfo, SubjectList

admin.site.register(SubjectList)

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'student_id', 'subject_list', 'address']

    # def subject_list(self, obj):
    #     return "\n".join([s.course_name for s in obj.subject.all()])