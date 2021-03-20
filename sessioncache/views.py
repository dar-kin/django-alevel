from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.contrib import messages


def add_to_session(func):
    def wrapper(self, request, *args, **kwargs):
        request.session["need_message"] = True
        return func(self, request, *args, **kwargs)
    return wrapper


class Task1View(LoginRequiredMixin, TemplateView):
    template_name = "session.html"

    @add_to_session
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class Task2View(LoginRequiredMixin, TemplateView):
    template_name = "cache.html"

    @add_to_session
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)



