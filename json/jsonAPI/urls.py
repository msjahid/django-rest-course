from django.urls import path
from .views import studentInfoAPI, studentListDetail
#
urlpatterns = [
    path('', studentInfoAPI, name='studentList'),
    path('<int:pk>', studentListDetail, name='student_details'),
]