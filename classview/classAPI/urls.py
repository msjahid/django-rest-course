from django.urls import path
from .views import StudentListAV, StudentDetailAV

urlpatterns = [
    # function based views url
    # path('', student_list, name='list_student'),
    path('', StudentListAV.as_view(), name='list_student'),
    path('<int:pk>', StudentDetailAV.as_view(), name='details_student'),
]