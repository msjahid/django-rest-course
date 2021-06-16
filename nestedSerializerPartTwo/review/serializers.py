from .models import Student, Subject, Teacher, Review
from rest_framework import serializers



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['course_name', 'course_code']


class TeacherSerializer(serializers.ModelSerializer):
    subject_ids = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ["teacher_name", "type", "subject_ids"]


class StudentSerializer(serializers.ModelSerializer):
    subject_list = SubjectSerializer(many=True, read_only=True)
    teacher_list = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['student_id', 'student_name', 'subject_list', 'teacher_list']


class ReviewSerializer(serializers.ModelSerializer):
    teacher_list = TeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

