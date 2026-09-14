from django.contrib import admin
from .models import Movie, Review, Report
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
admin.site.register(Review)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Report)
# Register your models here.
