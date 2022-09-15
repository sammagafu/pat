from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from . models import User,UserMembership,Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar']

class UserSerializer(serializers.ModelSerializer):
    avatar = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('first_name','last_name',"middlename",
        'username','email','phone_number','avatar',
        'mctnumber','gender','region','organization'
        ,'profession','areaofwork','typeofmember','memberId',)
        write_only_fields = ['password']

