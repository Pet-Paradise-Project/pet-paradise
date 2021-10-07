from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("ownersignin", views.ownersignin),
    path("ownersignup", views.ownersignup),
    path("doctorsignin", views.doctorsignin),
    path("doctorsignup", views.doctorsignup),
    path("explore", views.explore),
    path("care", views.care),
]
