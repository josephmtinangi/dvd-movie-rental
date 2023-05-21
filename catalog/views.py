from django.shortcuts import render
from .models import Movie, Director, Rental, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):

	num_movies = Movie.objects.all().count()
	num_rentals = Rental.objects.all().count()

	num_rentals_available = Rental.objects.filter(status__exact='a').count()

	num_directors = Director.objects.count()

	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'num_movies': num_movies,
		'num_rentals': num_rentals,
		'num_rentals_available': num_rentals_available,
		'num_directors': num_directors,
		'num_visits': num_visits,
	}

	return render(request, 'index.html', context=context)

def about(request):
	return render(request, 'about.html')

class MovieListView(generic.ListView):
	model = Movie
	paginate_by = 2


class MovieDetailView(generic.DetailView):
	model = Movie


class RentedMoviesByUserListView(LoginRequiredMixin, generic.ListView):
	model = Rental
	template_name = 'catalog/rental_list_user.html'
	paginate_by = 10

	def get_queryset(self):
		return (
			Rental.objects.filter(borrower=self.request.user)
			 .filter(status__exact='o')
			 .order_by('due_back')
		)
