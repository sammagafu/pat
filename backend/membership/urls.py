from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

profilerouter = DefaultRouter()
profilerouter.register('',views.ProfileViewSet, basename="Profile")

user_router = DefaultRouter()
user_router.register('',views.ProfileViewSet, basename="User")

urlpatterns = [
    path('',include(user_router.urls)),
    path('profile/',include(profilerouter.urls)),
    # path('profile/',views.ProfileUpdate.as_view()),
    # path('<int:pk>',views.UserDetailView.as_view()),
    # path('<str:memberId>',views.SpecificUserView.as_view())
]
