from .models import StudentInfo
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = StudentInfo
        fields = '__all__'

    def get_len_name(self, object):
        return len(object.name)

    def validate_name(self, value):

        if len(value) < 5:
            raise serializers.ValidationError("Name is not ordering!")
        else:
            return value

    def validate(self, data):
        if data['name'] == data['address']:
            raise serializers.ValidationError('Name and Address should be different')
        else:
            return data