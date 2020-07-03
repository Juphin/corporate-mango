
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:id>-<slug:slug>', views.detail, name="detail"),
    path('about', views.about, name="about")
]
