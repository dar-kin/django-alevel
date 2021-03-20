from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.contrib import messages


class SessionCacheMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_response(self, request, responce):
        session_count = request.session.get("count", 0)
        session_count += 1
        if session_count >= 4:
            session_count = 0
        request.session["count"] = session_count
        cache_count = cache.get("count", 0)
        cache_count += 1
        if cache_count >= 10:
            cache_count = 0
        cache.set("count", cache_count)
        request.session["cache_count"] = cache_count

        if request.session.get("need_message", False):
            del request.session["need_message"]
            if session_count == 0:
                messages.success(request, "first success")
            if cache_count == 0:
                messages.success(request, "second success")


        return responce
