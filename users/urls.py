from django.urls import path
from .views import users

app_name = "users"

urlpatterns = [
    path("<int:user_id>", users, name="user_id"),
    path("", users, name="users"),
]