from django.urls import path
from . import views
urlpatterns = [
    path('',views.ResourcesList.as_view()),
    path('<str:slug>',views.ResourcesDetailView.as_view())
]
