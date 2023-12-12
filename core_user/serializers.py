from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth.hashers import make_password


class MyUserCreateSerializer(ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    
    
    def validate_password(self, value):
        '''Hash password'''
        return make_password(value)
        
    class Meta(UserCreateSerializer.Meta):
        fields = [
            'email',
            'first_name',
            'last_name',
            'password'
        ]

