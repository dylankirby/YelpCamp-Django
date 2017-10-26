from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class Campground(models.Model):
	author = models.ForeignKey('auth.User' , related_name='submitted_campgrounds')
	name = models.CharField(max_length=128, blank=False, unique=True)
	image = models.URLField(blank=False)
	short_description = models.CharField(max_length=128)
	price_per_night = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
	city = models.CharField(max_length=56, blank=True, unique=False)

	PROVINCES = (
		('British Columbia', 'BC'),
		('Alberta','AB'),
		('Saskatchewan','SK'),
		('Manitoba','MB'),
		('Ontario','ON'),
		('Quebec','QC'),
		('New Brunswick','NB'),
		('Newfoundland and Labrador','NL'),
		('Nova Scotia','NS'),
		('Prince Edward Island','PEI'),
		('Yukon','YK'),
		('Northwest Territories','NT'),
		('Nunavut','NU'),
	)

	province = models.CharField(max_length=56, blank=False, unique=False, choices=PROVINCES, default='BC')


	def __init__(self, *args, **kwargs):
	    super(Campground, self).__init__(*args, **kwargs)
	    #write logic to custom field, pull all reviews and average

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('campgrounds:all')

class Review(models.Model):
	author = models.ForeignKey('auth.User', related_name='my_reviews', unique=True)
	campground = models.ForeignKey(Campground, related_name='reviews')
	comment = models.CharField(max_length=256, blank=True)

	RATINGS = (
		(1, 'Bad (1)'),
		(2, 'Ok (2)'),
		(3, 'Average (3)'),
		(4, 'Good (4)'),
		(5, 'Great (5)'),
	)
	rating = models.IntegerField(default=5, choices=RATINGS)
	date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse('campgrounds:all')

