from django.contrib import admin

from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('link', 'link_id')
    list_display_links = ('link', 'link_id')
    search_fields = ('link', 'link_id')
    readonly_fields = ['link_id']
