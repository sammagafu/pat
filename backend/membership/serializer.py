from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from . models import User

from djoser.serializers import  UserCreateSerializer as BaseUserCreateSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','typeofmember','memberId','gender','region','organization','profession','areaofwork','typeofmember','mctnumber','avatar','collage','year','get_avatar')
        write_only_fields = ['password']
        read_only_fields = ['get_avatar']

class UserSerializerCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('first_name','last_name',"middle_name",'email','phone','typeofmember','memberId','gender','region','organization','profession','areaofwork','typeofmember','mctnumber','avatar','collage','year')
        read_only_fields = ['get_avatar']
        write_only_fields = ['password']

