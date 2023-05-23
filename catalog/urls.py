from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about', views.about, name='about'),
	path('movies/', views.MovieListView.as_view(), name='movies'),
	path('movies/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
	path('mymovies/', views.RentedMoviesByUserListView.as_view(), name='my-rentals'),
	path('all-rented', views.RentedMoviesListView.as_view(), name='all-rented'),
	path('movie/<uuid:pk>/renew/', views.renew_movie_staff, name='renew-movie-staff'),
]
