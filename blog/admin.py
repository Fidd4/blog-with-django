from django.contrib import admin

from .models import Tag, Post


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tag, TagAdmin)
admin.site.register(Post)
