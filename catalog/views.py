import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewMovieForm

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
	paginate_by = 10


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

class RentedMoviesListView(LoginRequiredMixin, generic.ListView):
	model = Rental
	template_name = 'catalog/rental_list.html'
	paginate_by = 10

	def get_queryset(self):
		return (
			Rental.objects.order_by('due_back')
		)

@login_required
#@permission_required('catalog.can_mark_returned', raised_exception=True)
def renew_movie_staff(request, pk):
	rental = get_object_or_404(Rental, pk=pk)

	if request.method == 'POST':
		form = RenewMovieForm(request.POST)

		if form.is_valid():

			rental.due_back = form.cleaned_data['renewal_date']
			rental.save()

			return HttpResponseRedirect(reverse('all-rented'))

	else:
		proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
		form = RenewMovieForm(initial={'renewal_date': proposed_renewal_date})

	context = {
		'form': form,
		'rental': rental,
	}

	return render(request, 'catalog/movie_renew_staff.html', context)
