from django.shortcuts import render
from .models import Movie, Director, Rental, Genre, Language

# Create your views here.
def index(request):

	num_movies = Movie.objects.all().count()
	num_rentals = Rental.objects.all().count()

	num_rentals_available = Rental.objects.filter(status__exact='a').count()

	num_directors = Director.objects.count()

	context = {
		'num_movies': num_movies,
		'num_rentals': num_rentals,
		'num_rentals_available': num_rentals_available,
		'num_directors': num_directors
	}

	return render(request, 'index.html', context=context)
