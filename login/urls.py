from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("login", login_page),
]

handler404 = pageNotFound