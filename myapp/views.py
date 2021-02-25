from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    return HttpResponse("Hello")


def phone(request, phone_number):
    return HttpResponse(phone_number)


def trash(request, some_trash):
    return HttpResponse(some_trash)