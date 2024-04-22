from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)} # sirve para que mientras escribimos el titulo se llene automaticamente el campo de slug
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']