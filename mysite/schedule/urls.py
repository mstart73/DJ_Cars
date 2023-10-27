from django.urls import path

from . import views

urlpatterns = [
    path("/<str:dt>/", views.show_schedule, name="show_schedule"),

]