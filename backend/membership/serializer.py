from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from . models import User

from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

class UserSerializerCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','typeofmember','memberId','password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name',"middle_name",'email','phone','memberId')
        write_only_fields = ['password']