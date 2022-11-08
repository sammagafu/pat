from django.shortcuts import render
from rest_framework import generics
from rest_framework import status, authentication, permissions
from .serializers import ActivityRequestSerializer,ActivityRequestDetailsSerializer
from .models import ActivityRequest,ActivityRequestDetails

# Create your views here.
class CreateActivityRequest(generics.ListCreateAPIView):
    queryset = ActivityRequest.objects.all()
    serializer_class = ActivityRequestSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     product_slug  = self.request.data.get("product", None)  # read data from request
    #     producttosave = Product.objects.get(slug__exact=product_slug)
    #     serializer.save(owner=self.request.user,product=producttosave)
    
    def retrieve(self,request, *args, **kwargs):
        return self.queryset.filter(requestedbby=self.request.user)



class ActivityRequest(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActivityRequest.objects.all()
    serializer_class = ActivityRequestSerializer
    lookup_field = "slug"
    # permission_classes = [permissions.IsAuthenticated]


