from django.urls import path
from . import views

urlpatterns = [
    path('',views.UpdateList.as_view()),
    path('<str:slug>',views.UpdateDetailView.as_view())

]