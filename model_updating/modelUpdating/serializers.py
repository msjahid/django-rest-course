from .models import StudentInfo, SubjectList
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectList
        fields = ['id', 'course_name', 'date', 'day', 'month', 'year']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentInfo
        fields = '__all__'