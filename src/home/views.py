from platform import system

from django.shortcuts import render

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
