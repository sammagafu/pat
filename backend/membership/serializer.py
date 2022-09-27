from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from . models import User,Profile

from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

class UserSerializerCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','typeofmember','memberId','password')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['gender','region','organization','profession','areaofwork','mctnumber','collage','year','get_avatar']
        write_only_fields = 'avatar'

class UserSerializer(BaseUserCreateSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','memberId','profile')
        write_only_fields = ['password']