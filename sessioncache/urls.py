from django.urls import path
from.views import Task1View, Task2View


app_name = "session"


urlpatterns = [
    path("session", Task1View.as_view(), name="task1"),
    path("cache", Task2View.as_view(), name="task2"),
]