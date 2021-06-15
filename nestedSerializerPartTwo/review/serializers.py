from .models import StudentInfo, SubjectList, TeacherInfo
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectList
        fields = "__all__"

#HyperlinkedModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    subject_list = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = StudentInfo
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    course_list = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherInfo
        fields = "__all__"

