from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProjectsList.as_view()),
    path('<str:slug>',views.ProductsDetailView.as_view())

]