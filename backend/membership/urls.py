from django.urls import path
from . import views
urlpatterns = [
    path('',views.UsersList.as_view()),
    # path('<str:slug>',views.ResourcesDetailView.as_view())
]
