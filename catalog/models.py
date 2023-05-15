from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a movie genre (e.g. Action)')

	def __str__(self):
		return self.name


class Language(models.Model):
	name = models.CharField(max_length=200, help_text="Enter the movie's natural language")

	def __str__(self):
		return self.name


class Movie(models.Model):
	title = models.CharField(max_length=200)
	director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the movie')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')
	language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])


class Rental(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular movie')
	movie = models.ForeignKey('Movie', on_delete=models.RESTRICT, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='m',
		help_text='Movie availability',
	)

	class Meta:
		ordering = ['due_back']

	def __str__(self):
		return f'{self.id} ({self.book.title})'


class Director(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('director-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'

