from platform import system
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render



def elmuse(request):
    return render(request, "elmuse.html",)


def index(request):
    return render(request, "index.html",)


def eng_index(request):
    return render(request, "eng.html",)


def ru_index(request):
    return render(request, "ru.html",)

# Create your views here.
