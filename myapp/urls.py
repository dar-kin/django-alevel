from django.urls import path, re_path
from .views import hello_view, phone, trash
from misc.misc import generate_ukr_mobile_regex


app_name = "myapp"

urlpatterns = [
    re_path(generate_ukr_mobile_regex(), phone, name="phone"),
    re_path(r"(?P<some_trash>[a-f1-9]{4}-[a-f1-9]{6})/$", trash, name="trash"),
    path("", hello_view, name="hello"),
]
