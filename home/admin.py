from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Product) ❌

# 🎯 adminview  shortcut
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('procode','title','brand','added_on')
    ordering = ('brand',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',
    'is_published','created_on')
