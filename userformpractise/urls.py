from django.urls import path
from .views import task1, success_message, fail_message, login_view, logout_view, \
    registration_view, password_change_view, password_change_success, search_comments


app_name = "userformpractise"

urlpatterns = [
    path("task1/", task1, name="task1"),
    path("success_message/", success_message, name="success_message"),
    path("fail_message/", fail_message, name="fail_message"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", registration_view, name="register"),
    path("password_change/", password_change_view, name="password_change"),
    path("password_change_success/", password_change_success, name="password_change_success"),
    path("comments/", search_comments, name="comments"),
]
