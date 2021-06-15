from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import StudentInfo, SubjectList, TeacherInfo, Review
from .serializers import StudentSerializer, SubjectSerializer, TeacherSerializer, ReviewSerializer


class SubjectListAV(APIView):
    def get(self, request):
        subject = SubjectList.objects.all()
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
            subject = SubjectList.objects.get(pk=pk)
        except SubjectList.DoesNotExist:
            return Response({'Error': 'Subject info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(subject, context={'request': request})
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
            student = StudentInfo.objects.get(pk=pk)
        except StudentInfo.DoesNotExist:
            return Response({'Error': 'Student info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, context={'request': request})
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


class TeacherListAV(APIView):
    def get(self, request):
        teacher = TeacherInfo.objects.all()
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
            teacher = TeacherInfo.objects.get(pk=pk)
        except TeacherInfo.DoesNotExist:
            return Response({'Error': 'Teacher info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(teacher, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = TeacherInfo.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = TeacherInfo.objects.get(pk=pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class reviewListAV(APIView):
    def get(self, request):
        review = ReviewInfo.objects.all()
        serializer = ReviewSerializer(review, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class reviewDetailsAV(APIView):

    def get(self, request, pk):
        try:
            review = ReviewInfo.objects.get(pk=pk)
        except ReviewInfo.DoesNotExist:
            return Response({'Error': 'Review info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        review = ReviewInfo.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = ReviewInfo.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

