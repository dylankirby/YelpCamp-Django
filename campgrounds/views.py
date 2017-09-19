from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from campgrounds.models import Campground
# Create your views here.

class CreateCampground(LoginRequiredMixin,generic.CreateView):
	fields = ('name', 'image', 'description')
	model = Campground

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(CreateCampground, self).form_valid(form)

class CampgroundDetail(generic.DetailView):
	model = Campground

class CampgroundList(generic.ListView):
	model = Campground


