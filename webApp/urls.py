from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_view, name = "landing"),
    path('/refugee_register', views.register_refugee_view, name = "register_refugee"),
    path('/volunteer_register', views.register_volunteer_view, name = "register_volunteer"),
]