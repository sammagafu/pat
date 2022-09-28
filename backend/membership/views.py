import email
from rest_framework import generics
from . models import User,Profile
from .serializer import UserProfileSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


# class SpecificUserView(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = UserProfileSerializer
#     lookup_field = 'memberId'

class ProfileUpdate(APIView):
    def post(self, request):
        # print(request.data("email"))
        userdata = User.objects.filter(email=request.data.get("email"))
        print(userdata)
        # userprofile = Profile.objects.filter(user=user.pk).get()
        # print(userprofile)



# @api_view(['POST'])
# def get_my_team(request):
#      # print("request")
#      member = Team.objects.filter(teammember__pk=request.user.id).get()
#      company = CompanyInformation.objects.filter(team__pk=member.pk).get()

#      serializer = UserProfileSerializer(company)
#      return Response(serializer.data)