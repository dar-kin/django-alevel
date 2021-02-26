from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    return render(request, "hello.html", {"hello": "hello"})


def phone(request, phone_number):
    return render(request, "phone.html", {"phone": phone_number})


def trash(request, some_trash):
    return render(request, "trash.html", {"trash": some_trash})
