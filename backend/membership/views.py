import email
from rest_framework import generics, viewsets, mixins
from . models import User
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


# # class SpecificUserView(generics.RetrieveAPIView):
# #     queryset = Profile.objects.all()
# #     serializer_class = UserProfileSerializer
# #     lookup_field = 'memberId'

# class ProfileUpdate(APIView):
#     def post(self, request):
#         userdata = User.objects.filter(email=self.request.data.get('email')).get()
#         userprofile = User.objects.filter(user=userdata.pk).get()


# # @api_view(['POST'])
# # def get_my_team(request):
# #      # print("request")
# #      member = Team.objects.filter(teammember__pk=request.user.id).get()
# #      company = CompanyInformation.objects.filter(team__pk=member.pk).get()

# #      serializer = UserProfileSerializer(company)
# #      return Response(serializer.data)

class ProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','post','retrieve','put','patch']

    class UserViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.

        """
        queryset = User.objects.all()
        serializer_class = UserSerializer
        http_method_names = ['get','post','retrieve','put','patch']
