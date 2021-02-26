from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("archives/", views.archive, name="archive"),
    path("<int:article_number>/archives/", views.archive, name="article_number_archives"),
    path("<int:article_number>/<slug:article_slug>/", views.articles, name="article_number_slug"),
    path("<int:article_number>/", views.articles, name="article_number"),
    path("<slug:article_slug>/", views.articles, name="article_slug"),
    path("", views.articles, name="articles"),
]