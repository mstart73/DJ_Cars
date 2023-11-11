from django.urls import path
from django import views
from .views import uppermenu

urlpatterns = [

    path("", uppermenu, name="uppermenu"),
]