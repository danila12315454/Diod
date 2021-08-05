from django.http import HttpResponse
from django.shortcuts import render


def login_page(reqest):
    return render(reqest, "login/login_page.html")

def pageNotFound(reqest, exception):
    return HttpResponse(f"<h1>Либо ты проебався либ о я еблан;(</h1>")