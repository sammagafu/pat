from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from . models import User,UserMembership

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name',"middlename",
        'username','email','phone_number','avatar',
        'mctnumber','gender','region','organization'
        ,'profession','areaofwork','typeofmember','memberId','avatar','collage','year')
        write_only_fields = ['password']

