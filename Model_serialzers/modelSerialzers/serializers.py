from .models import StudentInfo
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentInfo
        # fields = '__all__' for all fields
        # we can not use both fields and exclude
        # ----> fields = ['id', 'name', 'studentId', 'address']
        exclude = ['studentId'] # We dont show the student ID

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