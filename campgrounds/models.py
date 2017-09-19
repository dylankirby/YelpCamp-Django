from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Campground(models.Model):
	author = models.ForeignKey('auth.User' , related_name='submitted_campgrounds')
	name = models.CharField(max_length=128, blank=False, unique=True)
	image = models.URLField(blank=False)
	description = models.TextField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('campgrounds:all')







