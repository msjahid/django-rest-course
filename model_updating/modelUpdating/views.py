from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import StudentInfo, SubjectList
from .serializers import StudentSerializer, SubjectSerializer


class SubjectListAV(APIView):
    def get(self, request):
        subject = SubjectList.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class SubjectDetailsAV(APIView):

    def get(self, request, pk):
        try:
            subject = SubjectList.objects.get(pk=pk)
        except SubjectList.DoesNotExist:
            return Response({'Error': 'Subject info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        subject = SubjectList.objects.get(pk=pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = SubjectList.objects.get(pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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