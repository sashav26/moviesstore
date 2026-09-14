from django.contrib import admin
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
admin.site.register(Review)
admin.site.register(Movie, MovieAdmin)
# Register your models here.
