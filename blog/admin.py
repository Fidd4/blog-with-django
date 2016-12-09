# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title_post', 'draft', 'posted')
    list_filter = ('draft', 'posted', 'tags')
    search_fields = ['title_post']
    fieldsets = (
        (None, {
            'fields': (
                'title_page',
                'title_post',
                'draft',
                'preview',
                'text',
                'posted',
                'tags',
            )
        }),
        ('Метаданные', {
            'classes': ('collapse',),
            'fields': ('description', 'keywords'),
        }),
    )


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
