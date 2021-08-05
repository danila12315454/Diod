from django.http import HttpResponse
from django.shortcuts import render

def index(reqest):
    return HttpResponse("Ну а хули и да")


def id_reqest(reqest, id):
    return HttpResponse(f"<h1>Ну тип вот число</h1><p>{id * 100}</p>")

def archive(reqest, year):
        return HttpResponse(f"<h1>Ну тип вот год</h1><p>{year}</p>")

def pageNotFound(reqest, exception):
    return HttpResponse(f"<h1>Либо ты проебався либ о я еблан;(</h1>")