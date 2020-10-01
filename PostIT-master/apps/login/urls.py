from django.urls import path
from .views import indexPage, logoutUser, changeEmail, changePass, settingsUser,changeUsername

urlpatterns = [
    path("", indexPage, name="index"),
    path("logout/", logoutUser, name="logout"),
    path("settings/", settingsUser, name="settings"),
    path("changePass/", changePass, name="changePass"),
    path("changeEmail/", changeEmail, name="changeEmail"),
    path("changeUsername/", changeUsername, name="changeUsername"),
]
