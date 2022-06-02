from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):

    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=50)
    occupation = serializers.CharField(max_length=50)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', '')
        data['gender'] = self.validated_data.get('gender', '')
        data['occupation'] = self.validated_data.get('occupation', '')

        return data