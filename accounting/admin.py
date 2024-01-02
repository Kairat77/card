from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_url', 'content_file')
    fields = ('title', 'content_url', 'content_file')