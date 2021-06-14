from .models import StudentInfo, SubjectList
from rest_framework import serializers


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectList
        fields = ['course_name', 'course_code']

# # StringRelatedField, PrimaryKeyRelatedField, HyperlinkedRelatedField
class StudentSerializer(serializers.ModelSerializer):
    # subject_list = SubjectSerializer(many=True, read_only=True)
    # subject_list = serializers.StringRelatedField(many=True)
    # subject_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # PrimaryKeyRelatedField is default
    subject_list = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='details_subject'
    )

    class Meta:
        model = StudentInfo
        fields = ['name', 'student_id', 'address', 'subject_list']
