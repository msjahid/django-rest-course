from django.urls import path
from .views import StudentListAV, StudentDetailAV, SubjectListAV, SubjectDetailsAV

urlpatterns = [
    path('student/', StudentListAV.as_view(), name='list_student'),
    path('student/<int:pk>/', StudentDetailAV.as_view(), name='details_student'),
    path('subject/', SubjectListAV.as_view(), name='list_subject'),
    path('subject/<int:pk>/', SubjectDetailsAV.as_view(), name='details_subject'),

]