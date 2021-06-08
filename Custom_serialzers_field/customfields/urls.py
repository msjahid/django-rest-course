from django.urls import path
from .views import StudentListAV, StudentDetailAV

urlpatterns = [
    path('', StudentListAV.as_view(), name='list_student'),
    path('<int:pk>', StudentDetailAV.as_view(), name='details_student'),
]