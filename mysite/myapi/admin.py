from django.contrib import admin
from .models import Title, Volume, Chapter, Tag


class TitleAdmin(admin.ModelAdmin):
    search_fields = ['ru_name', 'en_name', 'alt_name']


admin.site.register(Title, TitleAdmin)
admin.site.register(Volume)
admin.site.register(Chapter)
admin.site.register(Tag)
