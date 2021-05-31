from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import StudentInfo
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = StudentInfo.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def students_details(request, pk):
    if request.method == 'GET':
        try:
            student = StudentInfo.objects.get(pk=pk)
        except StudentInfo.DoesNotExist:
            return Response({'Error': 'Student info not in there'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    if request.method == 'PUT':
        student = StudentInfo.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        student = StudentInfo.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
