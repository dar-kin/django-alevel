from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["name", "authors", "available"]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name"]


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name"]


@admin.register(models.TakenBook)
class TakenBookAdmin(admin.ModelAdmin):
    fields = ["book", "client"]
