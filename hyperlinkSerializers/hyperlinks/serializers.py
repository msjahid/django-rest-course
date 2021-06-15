from .models import StudentInfo, SubjectList
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectList
        fields = "__all__"

#HyperlinkedModelSerializer
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    subject_list = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = StudentInfo
        fields = "__all__"