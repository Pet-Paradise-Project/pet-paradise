from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from threading import Timer
from .models import *

# from django_email_verification import send_email

# Create your views here.
def index(request):
    return render(request, "index.html")


def ownersignup(request):
    if request.method == "POST":
        yourname = request.POST["yourname"]
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["password1"]
        email = request.POST["email"]
        contact = request.POST["contact"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                mess = "Username is already taken."
                return render(request, "ownersignup.html", {"mess": mess})
            elif User.objects.filter(email=email).exists():
                mess = "Email is already taken."
                return render(request, "ownersignup.html", {"mess": mess})
            else:
                user = User.objects.create_user(
                    email=email, username=username, password=password1
                )
                user1 = User.objects.get(username=username)
                # t = Timer(900.0, selfDestruct, [user1.username])
                # t.start()
                # user.is_active = False  # Example
                # send_email(user)
                owner = petOwner(
                    username=username,
                    yourname=yourname,
                    email=email,
                    contact=contact,
                    user=user,
                )
                owner.save()
                mess1 = "Please check your mail inbox to verify your account. Link will expire in 15 mins"
                return render(request, "ownersignin.html", {"mess1": mess1})
        else:
            mess = "Password is incorrect."
            return render(request, "ownersignup.html", {"mess": mess})
    else:
        return render(request, "ownersignup.html")


def checkowner(username):
    owner = petOwner.objects.all()
    for u in owner:
        if username == u.username:
            return True
    return False


def checkdoctor(username):
    doctor = petDoctor.objects.all()
    for u in doctor:
        if username == u.username:
            return True
    return False


def ownersignin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if checkowner(username):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                mess = "Invalid Credentials."
                return render(request, "ownersignin.html", {"mess": mess})
        else:
            mess = "Invalid Credentials."
            return render(request, "ownersignin.html", {"mess": mess})
    else:
        return render(request, "ownersignin.html")


def doctorsignin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if checkdoctor(username):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                mess = "Invalid Credentials."
                return render(request, "doctorsignin.html", {"mess": mess})
        else:
            mess = "Invalid Credentials."
            return render(request, "doctorsignin.html", {"mess": mess})
    else:
        return render(request, "doctorsignin.html")


def doctorsignup(request):
    if request.method == "POST":
        yourname = request.POST["yourname"]
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["password1"]
        email = request.POST["email"]
        contact = request.POST["contact"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                mess = "Username is already taken."
                return render(request, "doctorsignup.html", {"mess": mess})
            elif User.objects.filter(email=email).exists():
                mess = "Email is already taken."
                return render(request, "doctorsignup.html", {"mess": mess})
            else:
                user = User.objects.create_user(
                    email=email, username=username, password=password1
                )
                user1 = User.objects.get(username=username)
                # t = Timer(900.0, selfDestruct, [user1.username])
                # t.start()
                # user.is_active = False  # Example
                # send_email(user)
                doctor = petDoctor(
                    username=username,
                    yourname=yourname,
                    email=email,
                    contact=contact,
                    user=user,
                )
                doctor.save()
                mess1 = "Please check your mail inbox to verify your account. Link will expire in 15 mins"
                return render(request, "doctorsignin.html", {"mess1": mess1})
        else:
            mess = "Password is incorrect."
            return render(request, "doctorsignup.html", {"mess": mess})
    else:
        return render(request, "doctorsignup.html")


def explore(request):
    return render(request, "explore.html")


def care(request):
    return render(request, "care.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


# def selfDestruct(username):
#     user = User.objects.get(username=username)
#     if user.is_active == True:
#         pass
#     else:
#         user.delete()


def cat(request):
    return render(request, "cat.html")


def dog(request):
    return render(request, "dog.html")


def food(request):
    return render(request, "food.html")


def products(request):
    return render(request, "products.html")


def medicine(request):
    return render(request, "medicine.html")