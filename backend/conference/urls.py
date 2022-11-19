from django.urls import path
from . import views

urlpatterns = [
    path('',views.ConferenceListView.as_view()),
    path('<str:slug>',views.ConferenceDetailView.as_view())

]