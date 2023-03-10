from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:player>", views.player_by_number),
    path("<str:player>", views.player_text)
]