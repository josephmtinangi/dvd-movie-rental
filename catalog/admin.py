from django.contrib import admin

# Register your models here.
from .models import Director, Genre, Language, Movie, Rental

#admin.site.register(Movie)
#admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)

class DirectorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth')

	fields = ['first_name', 'last_name', ('date_of_birth')]

admin.site.register(Director, DirectorAdmin)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'director', 'display_genre')


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
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
