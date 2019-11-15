from django.contrib import admin
from . import models

'''class CommentInline(admin.StackedInline):
    model=models.Comment'''
class CommentInline(admin.TabularInline):
    model=models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
    CommentInline,
    ]

# Register your models here.
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
