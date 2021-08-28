from django.urls import path
from .views import *


urlpatterns = [
    path("", redir.as_view(), name="login_page"),
    path("login/", login.as_view(), name="login_page"),
    path("profile/<str:login>", profile.as_view(), name="profile_page"),
    path("changedata/<str:login>", changedata.as_view(), name="changedata_page"),
    path("messenger/<str:login_id>/<str:chat_id>", messenger.as_view(), name="messenger_page"),
]

handler404 = pagenotfound
