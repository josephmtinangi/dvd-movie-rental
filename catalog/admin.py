from django.contrib import admin

# Register your models here.
from .models import Director, Genre, Language, Movie, Rental

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)

@admin.register(Rental)
class Rental(admin.ModelAdmin):
	list_display = ('movie', 'status', 'borrower', 'due_back', 'id')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
			'fields': ('movie', 'imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back', 'borrower')
		}),
	)
