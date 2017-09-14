from django.contrib import admin
from .models import Campground


class CampgroundInline(admin.TabularInline):
	model = Campground


# Register your models here.
admin.site.register(Campground)