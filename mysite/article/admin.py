from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_time', 'created_by')
    list_filter = ('description',)
admin.site.register(Item, ItemAdmin)


