from django.urls import path

from . import views

urlpatterns = [
    path("cars/", views.show_cars, name="show_cars"),

]