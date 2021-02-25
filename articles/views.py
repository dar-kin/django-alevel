from django.http import HttpResponse


def articles(request, article_number=None, article_slug=None):
    response = "Articles here. "
    if article_number:
        response += f"Number of article is {article_number}. "
    if article_slug:
        response += f"Slug of article is {article_slug}. "
    return HttpResponse(response)


def archive(request, article_number=None):
    response = "Archives here. "
    if article_number:
        response += f"Number of article is {article_number}. "
    return HttpResponse(response)
