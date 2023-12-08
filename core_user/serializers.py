from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer


class MyUserCreateSerializer(ModelSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        fields = [
            'email',
            'first_name',
            'last_name',
            'password'
        ]

