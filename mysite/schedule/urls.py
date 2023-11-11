from django.urls import path

from . import views

urlpatterns = [
    path("<str:dt>/", views.show_schedule, name="show_schedule"),
    path("", views.show_schedule, name="show_schedule"),
    path("", views.new_reservation, name="new_reservation"),
    path("", views.show_types, name="show_types"),
]