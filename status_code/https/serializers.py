from .models import StudentInfo
from rest_framework import serializers


# Student Information Serializer

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    studentId = serializers.IntegerField()
    address = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return StudentInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.studentId = validated_data.get('studentId', instance.studentId)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
