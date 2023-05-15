from django.contrib import admin

# Register your models here.
from .models import Director, Genre, Language, Movie, Rental

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Rental)
