from django.core.cache import cache


def get_count(request):
    return {"count": cache.get("count", 0)}
