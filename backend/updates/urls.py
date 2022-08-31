from django.urls import path
from . import views

urlpatterns = [
    path('',views.UpdateList.as_view()),

]