from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from chat.models import Message
from chat.serializers import MessageSerializer, UserSerializer
from rest_framework.parsers import JSONParser


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == "GET":
        messages = Message.objects.filter(
            sender_id=sender, receiver_id=receiver, is_read=False
        )
        serializer = MessageSerializer(
            messages, many=True, context={"request": request}
        )
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "GET":
        return render(
            request,
            "chat.html",
            {"users": User.objects.exclude(username=request.user.username)},
        )


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "GET":
        return render(
            request,
            "messages.html",
            {
                "users": User.objects.exclude(username=request.user.username),
                "receiver": User.objects.get(id=receiver),
                "messages": Message.objects.filter(
                    sender_id=sender, receiver_id=receiver
                )
                | Message.objects.filter(sender_id=receiver, receiver_id=sender),
            },
        )
    elif request.method == "POST":
        return render(
            request,
            "messages.html",
            {
                "users": User.objects.exclude(username=request.user.username),
                "receiver": User.objects.get(id=receiver),
                "messages": Message.objects.filter(
                    sender_id=sender, receiver_id=receiver
                )
                | Message.objects.filter(sender_id=receiver, receiver_id=sender),
            },
        )
