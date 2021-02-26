from django.http import HttpResponse
from django.shortcuts import render
from random import randint, choice
from string import ascii_lowercase


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
    article_id = randint(5, 10)
    article_slug = ''.join(choice(ascii_lowercase) for _i in range(article_id))
    return render(request, "main.html", {"article_id": article_id,
                                         "article_slug": article_slug})

