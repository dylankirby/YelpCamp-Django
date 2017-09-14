from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Campground(models.Model):
	author = models.ForeignKey(User, related_name='submitted_campgrounds')
	name = models.CharField(max_length=128, blank=False, unique=True)
	image = models.ImageField(upload_to='campground_images', blank=False)
	description = models.TextField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('campgrounds:single', kwargs={'pk':self.pk})


# from django.core.validators import MinValueValidator,MaxValueValidator

# class Reviews(models.Model):
# 	author = models.ForeignKey(User, related_name='my_comments')
# 	campgrounds = models.ForeignKey(Campground, related_name='comments')
# 	rating = models.IntergerField(validators=[MinValueValidator(0), MaxValueValidator(5)])




