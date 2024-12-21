from django.contrib import admin
from django.urls import path, include
from Hello_world import views

urlpatterns = [
  path("", views.index, name='home'),
]
