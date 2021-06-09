from .models import StudentInfo, SubjectList
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectList
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentInfo
        fields = '__all__'