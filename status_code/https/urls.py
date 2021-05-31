from django.urls import path
from .views import student_list, students_details

urlpatterns = [
    # function based views url
    # path('', student_list, name='list_student'),
    path('', student_list, name='list_student'),
    path('<int:pk>', students_details, name='details_student'),
]