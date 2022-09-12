from django.urls import path
from . import views
urlpatterns = [
    path('',views.UsersList.as_view()),
    path('<int:pk>',views.UserDetailView.as_view())
]
