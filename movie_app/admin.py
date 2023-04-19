from django.contrib import admin
from .models import Movie, Director


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'director']
    list_editable = ['rating', 'director', 'budget']

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director)