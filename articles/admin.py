from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'create_date')

    def create_date(self, obj):
        return obj.created
