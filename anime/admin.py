from django.contrib import admin
from .models import Anime, Rating

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "genre", "type", "episodes", "rating", "members")
    search_fields = ("name", "genre", "type")
    list_filter = ("genre", "type")
    ordering = ("-rating", "name")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "anime", "rating")
    search_fields = ("user__email", "anime__name")
    list_filter = ("rating",)
