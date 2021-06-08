from rest_framework.views import APIView
from .models import StudentInfo
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status


class StudentListAV(APIView):

    def get(self, request):
        students = StudentInfo.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StudentDetailAV(APIView):

    def get(self, request, pk):
        try:
            student = StudentInfo.objects.get(pk=pk)
        except StudentInfo.DoesNotExist:
            return Response({'Error': 'Student info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = StudentInfo.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = StudentInfo.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)