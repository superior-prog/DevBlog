from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog_title', 'date_posted',)
    search_fields = ('author',)
    readonly_fields = ('date_posted',)

    filter_horizontal = ()
    ordering = ('-date_posted',)
    fieldsets = ()
    list_filter = ('author',)


class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog_post', 'content', 'date_posted',)
    search_fields = ('author',)
    readonly_fields = ('date_posted',)

    filter_horizontal = ()
    ordering = ('-date_posted',)
    fieldsets = ()
    list_filter = ('author',)




admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register(BlogCommentModel, BlogCommentModelAdmin)
