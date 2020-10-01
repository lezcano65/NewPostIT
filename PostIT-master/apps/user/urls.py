from django.urls import path
from .views import *
from apps.login.views import *

urlpatterns = [
    path("home/", mostrar_notas, name="home"),
    path("home/home", mostrar_notas, name="home2"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("create/", newnota, name="create"),
    path("delete/<int:pk>/", deleteNote, name="delete"),
    path("informatorio/", informatorio, name="informatorio"),
]
