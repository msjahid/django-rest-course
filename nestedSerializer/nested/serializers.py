from .models import StudentInfo, SubjectList
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectList
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    subject_list = SubjectSerializer(many=True, read_only=True)

    class Meta:
        # depth = 4 Should not use
        model = StudentInfo
        fields = '__all__'