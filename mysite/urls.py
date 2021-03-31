from django.contrib import admin
from django.urls import path, include
from articles.views import main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls', namespace="myapp")),
    path("articles/", include('articles.urls', namespace='articles')),
    path("users/", include("users.urls", namespace="users")),
    path("userformpractise/", include("userformpractise.urls", namespace="userformpractise")),
    path('session/', include("sessioncache.urls", namespace="session")),
    path("api/", include("rest.urls")),
    path("", main, name="main"),
]
