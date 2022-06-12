from argparse import Namespace
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.landing_view, name = "landing"),
    path('refugee_register/', views.register_refugee_view, name = "refugee_register"),
    path('volunteer_register/', views.register_volunteer_view, name = "volunteer_register"),
    path('question/', views.question_view, name = "question"),
]

