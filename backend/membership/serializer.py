from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from . models import User,Profile

from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['gender','region','organization','profession','areaofwork','mctnumber','collage','year']
        write_only_fields = 'avatar',
        read_only = 'get_avatar'

class UserSerializer(BaseUserCreateSerializer):
    profile = UserProfileSerializer()
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','memberId','typeofmember','profile')
        write_only_fields = ['password']

class UserSerializerCreate(BaseUserCreateSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','typeofmember','memberId','password','profile')
