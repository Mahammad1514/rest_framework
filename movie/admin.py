from django.contrib import admin
from .models import Genre, Studio, Movie

# Register your models here.

admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Movie)
