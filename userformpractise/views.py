from django.shortcuts import render, redirect, reverse
from .forms import Task1Form, Task2LoginForm, Task3RegistrationForm, Task4PasswordChangeForm, Task56CommentSearchForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from task3.models import Comment


def task1(request):
    if request.method == "POST":
        form = Task1Form(request.POST)
        if form.is_valid():
            return redirect(reverse("userformpractise:success_message"))
        return redirect(reverse("userformpractise:fail_message"))
    else:
        form = Task1Form()
    return render(request, "task1.html", {"form": form})


def success_message(request):
    return HttpResponse("You succeed")


def fail_message(request):
    return HttpResponse("You failed")


def login_view(request):
    if request.method == "POST":
        form = Task2LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect(reverse("userformpractise:logout"))
    else:
        form = Task2LoginForm()
    return render(request, "task2login.html", {"form": form})


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect(reverse("userformpractise:login"))
    else:
        return render(request, "task2logout.html", {})


def registration_view(request):
    if request.method == "POST":
        form = Task3RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data["username"],
                                            password=form.cleaned_data["password"])
            login(request, user)
            return redirect(reverse("userformpractise:password_change"))
    else:
        form = Task3RegistrationForm()
    return render(request, "task3registration.html", {"form": form})


@login_required
def password_change_view(request):
    if request.method == "POST":
        form = Task4PasswordChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(form.cleaned_data["current_password"]):
                user.set_password(form.cleaned_data["password"])
                user.save()
                login(request, user)
                return redirect(reverse("userformpractise:password_change_success"))
            form.add_error("current_password", "Incorrect password")
    else:
        form = Task4PasswordChangeForm()
    return render(request, "task4change_password.html", {"form": form, "username": request.user.username})


@login_required
def password_change_success(request):
    return HttpResponse("Password successfully changed")


@login_required
def search_comments(request):
    form = Task56CommentSearchForm(request.GET)
    if form.is_valid():
        comments = Comment.objects.filter(text__icontains=form.cleaned_data.get("text"))
        if form.cleaned_data.get("is_user"):
            comments = comments.filter(user=request.user)
        return render(request, "comments.html", {"form": form, "comments": comments})
    else:
        return render(request, "comments.html", {"form": form})
