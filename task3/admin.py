from django.contrib import admin
from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["name", "text", "user"]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ["user", "text", "parent", "article"]


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Dislike)
class DislikeAdmin(admin.ModelAdmin):
    pass
