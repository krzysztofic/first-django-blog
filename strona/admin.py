from django.contrib import admin
from .models import Category, Post


class AdminPost(admin.ModelAdmin):
    list_display = ['author', 'title', 'status', 'created_date']
    list_display_links = ('title',)
    list_editable = ('status', )
    list_filter = ('status', 'categories',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category)
admin.site.register(Post, AdminPost)
