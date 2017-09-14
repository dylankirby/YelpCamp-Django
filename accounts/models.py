from django.db import models
from django.contrib import auth

# Create your models here.

#User model inherited form Django User class
class User(auth.models.User):

	def __str__(self):
		return self.username

