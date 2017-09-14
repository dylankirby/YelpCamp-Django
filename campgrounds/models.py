from django.db import models
from django.utils.text import slugify

# Create your models here.
import misaka

from django.contrib.auth import get_user_model

User = get_user_model()

from django import template
register = template.Library()

class Campground(models.Model):
	pass

