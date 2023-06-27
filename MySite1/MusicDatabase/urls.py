from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:idNum>", views.idAlbums),
    path("<str:sort>", views.indexWithSort)
]