from django.urls import path
from . import views
urlpatterns = [
    path('',views.UsersList.as_view()),
    path('<str:username>',views.UserDetailView.as_view())
]
