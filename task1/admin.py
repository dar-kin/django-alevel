from django.contrib import admin
from . import models


@admin.register(models.Author1)
class Author1Admin(admin.ModelAdmin):
    fields = ["first_name", "last_name"]


@admin.register(models.Book1)
class Book1Admin(admin.ModelAdmin):
    fields = ["name", "author"]
