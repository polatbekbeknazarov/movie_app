from django.contrib import admin
from .models import Director, Actor, Rating, Movie, Genre

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'value',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'director', 'rating',)
    prepopulated_fields = {'slug': ('title',)}
