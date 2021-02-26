from django.http import HttpResponse
from django.shortcuts import render


def articles(request, article_number=None, article_slug=None):
    response = {}
    if article_number:
        response["article_id"] = article_number
    if article_slug:
        response["article_slug"] = article_slug
    return render(request, "article.html", response)


def archive(request, article_number=None):
    response = {}
    if article_number:
        response["article_id"] = article_number
    return render(request, "archives.html", response)


def main(request):
    return render(request, "main.html")

