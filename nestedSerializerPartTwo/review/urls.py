from django.urls import path
from .views import StudentListAV, StudentDetailAV, SubjectListAV, SubjectDetailsAV, TeacherListAV, TeacherDetailsAV

urlpatterns = [
    path('student/', StudentListAV.as_view(), name='list_student'),
    path('student/<int:pk>/', StudentDetailAV.as_view(), name='studentinfo-detail'),
    path('subject/', SubjectListAV.as_view(), name='list_subject'),
    path('subject/<int:pk>/', SubjectDetailsAV.as_view(), name='subjectlist-detail'),
    path('teacher/', TeacherListAV.as_view(), name='list_teacher'),
    path('teacher/<int:pk>/', TeacherDetailsAV.as_view(), name='teacherlist-detail'),
]