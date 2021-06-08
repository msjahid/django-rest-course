from .models import StudentInfo
from rest_framework import serializers

#Validator

def id_length(value):
    if len(str(value)) < 100:
        raise serializers.ValidationError("Student ID can not over 100!")

# Student Information Serializer

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    studentId = serializers.IntegerField(validators=[id_length])
    address = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return StudentInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.studentId = validated_data.get('studentId', instance.studentId)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    # Field-level validation
    def validate_name(self, value):

        if len(value) < 5:
            raise serializers.ValidationError("Name is not ordering!")
        else:
            return value

    # Object-level validation
    def validate(self, data):
        if data['name'] == data['address']:
            raise serializers.ValidationError('Name and Address should be different')
        else:
            return data