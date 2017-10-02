from django.contrib import admin
from .models import Campground, Review


class CampgroundInline(admin.TabularInline):
	model = Campground


# Register your models here.
admin.site.register(Campground)
admin.site.register(Review)