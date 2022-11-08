from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateActivityRequest.as_view(),name="list"),
    path('<str:slug>/',views.ActivityRequest.as_view(),name="detail"),
]