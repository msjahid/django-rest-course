from .models import StudentInfo
from django.http import JsonResponse


# Create your views here.

def studentInfoAPI(request):
    data = {
        'student': list(StudentInfo.objects.all().values())
    }
    return JsonResponse(data)


def studentListDetail(request, pk):
    student_list = StudentInfo.objects.get(pk=pk)
    data = {
        'name': student_list.name,
        'studentId': student_list.studentId,
        'address': student_list.address
    }
    return JsonResponse(data)
