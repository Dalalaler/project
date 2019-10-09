from platform import system
from pathlib import Path
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response


def elmuse(request):
    return render(request, "elmuse.html", {
        "data": [
            "My Project",
            system(),
        ],
    })


def index(request):
    return render(request, "index.html", {
        "data": [
            "My Project",
            system(),
        ],
    })


def eng_index(request):
    return render(request, "eng.html", {
        "data": [
            "My Project",
            system(),
        ],
    })


def ru_index(request):
    return render(request, "ru.html", {
        "data": [
            "My Project",
            system(),
        ],
    })

# Create your views here.
