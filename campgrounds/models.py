from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Campground(models.Model):
	author = models.ForeignKey('auth.User' , related_name='submitted_campgrounds')
	name = models.CharField(max_length=128, blank=False, unique=True)
	image = models.URLField(blank=False)
	short_description = models.CharField(max_length=128)
	price_per_night = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('campgrounds:all')

class Review(models.Model):
	author = models.ForeignKey('auth.User', related_name='my_comments')
	campground = models.ForeignKey(Campground, related_name='comments')
	comment = models.CharField(max_length=256, blank=True)

	RATINGS = (
		('Bad (1)', 1),
		('Ok (2)', 2),
		('Average (3)', 3),
		('Good (4)', 4),
		('Great (5)', 5),
	)
	rating = models.IntegerField(default=5, choices=RATINGS)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('campgrounds:details', pk=campground.pk)



