from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    phone = serializers.CharField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, validators=[validate_password],style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('pk','email','password','first_name', 'middle_name', 'last_name','memberId',
         'phone','typeofmember','region','organization','profession','areaofwork','mctnumber','gender','avatar','collage','year','get_avatar','get_user_fullname','is_active','is_approved','is_staff')
        # read_only_fields = ('get_avatar','get_user_fullname','is_active','is_approved','is_staff')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone': {'required': True},
            'typeofmember': {'required': True},
            'region': {'required': True},
            'organization': {'required': True},
            'profession': {'required': True},
            'areaofwork': {'required': True},
        }
        

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], 
        validated_data['password']
        )
        user.phone = validated_data['phone']
        user.typeofmember = validated_data['typeofmember']
        user.region = validated_data['region']
        user.organization = validated_data['organization']
        user.profession = validated_data['profession']
        user.areaofwork = validated_data['areaofwork']
        user.mctnumber = validated_data['mctnumber']
        user.collage = validated_data['collage']
        user.year = validated_data['year']
        user.first_name = validated_data['first_name']
        user.middle_name = validated_data['middle_name']
        user.last_name  = validated_data['last_name']
        user.gender  = validated_data['gender']
        user.save()
        return user


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )

class UsersProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )