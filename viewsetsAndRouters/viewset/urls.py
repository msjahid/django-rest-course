from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (StudentListAV, StudentDetailAV, SubjectListAV, SubjectDetailsAV,
                    TeacherListAV, TeacherDetailsAV, ReviewList, ReviewDetail, ReviewCreate, StudentList)


router = DefaultRouter()
router.register('student', StudentList, basename='student-list')

urlpatterns = [

    path('', include(router.urls)),

    # path('student/', StudentListAV.as_view(), name='list_student'),
    # path('student/<int:pk>/', StudentDetailAV.as_view(), name='studentinfo-detail'),


    path('subject/', SubjectListAV.as_view(), name='list_subject'),
    path('subject/<int:pk>/', SubjectDetailsAV.as_view(), name='subjectlist-detail'),

    path('teacher/', TeacherListAV.as_view(), name='list_teacher'),
    path('teacher/<int:pk>/', TeacherDetailsAV.as_view(), name='teacherlist-detail'),
    # path('review/', ReviewList.as_view(), name='list_review'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='reviewlist-detail'),

    path('teacher/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('teacher/<int:pk>/review/', ReviewList.as_view(), name='list_review'),
    path('teacher/review/<int:pk>/', ReviewDetail.as_view(), name='reviewlist-detail'),
]