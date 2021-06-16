from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Student, Subject, Teacher, Review
from .serializers import StudentSerializer, SubjectSerializer, TeacherSerializer, ReviewSerializer
from rest_framework import mixins
from rest_framework import generics



class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
        #     # teachers = Teacher.objects.filter(subject_ids=student.id)
        #     teachers = Teacher.objects.filter(subject_ids=student.id).values('teacher_name', 'type', 'subject_ids')
        #     # for k in teachers:
        #     #     print(k,type(k))
        #     serializer = StudentSerializer(student, context={'request': request})
        #     # teacher_response_serializer.is_valid(raise_exception=True)
        #     # print('line 76', teachers)
        #     # print('line 72', teacher_response_serializer.data['teacher_name'])
        except Student.DoesNotExist:
            return Response({'Error': 'Student info not in there'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)
        # return Response(
        #         {
        #             # "id": student.id,
        #             # "student_name": student.student_name,
        #             # "student_id": student.student_id,
        #             # "subject_ids": student.subject_ids,
        #             # "address": student.address,
        #             "student": serializer.data,
        #             "teachers": teachers
        #         }
        #     )

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


# class ReviewListAV(APIView):
#     def get(self, request):
#         review = Review.objects.all()
#         serializer = ReviewSerializer(review, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class ReviewDetailsAV(APIView):
#
#     def get(self, request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Response({'Error': 'Review info not in there'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = ReviewSerializer(review, context={'request': request})
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         review = Review.objects.get(pk=pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

