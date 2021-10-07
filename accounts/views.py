from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def ownersignin(request):
    return render(request, "ownersignin.html")


def ownersignup(request):
    return render(request, "ownersignup.html")


def doctorsignin(request):
    return render(request, "doctorsignin.html")


def doctorsignup(request):
    return render(request, "doctorsignup.html")


def explore(request):
    return render(request, "explore.html")


def care(request):
    return render(request, "care.html")
