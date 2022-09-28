from django.urls import path
from . import views
urlpatterns = [
    path('profile/',views.ProfileUpdate.as_view()),
    # path('<int:pk>',views.UserDetailView.as_view()),
    # path('<str:memberId>',views.SpecificUserView.as_view())
]
