from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Student, Subject, Teacher, Review
from .serializers import StudentSerializer, SubjectSerializer, TeacherSerializer, ReviewSerializer
from rest_framework import generics


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SubjectListAV(APIView):
    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True, context={'request': request})
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
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({'Error': 'Subject info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(subject, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentListAV(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True, context={'request': request})
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
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'Error': 'Student info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)


    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherListAV(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TeacherDetailsAV(APIView):

    def get(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Response({'Error': 'Teacher info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
