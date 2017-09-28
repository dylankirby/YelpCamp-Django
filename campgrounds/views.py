from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.views import generic
from campgrounds.models import Campground,Review


# Campground Views
class CreateCampground(LoginRequiredMixin, generic.CreateView):
	fields = ('name', 'image', 'short_description', 'price_per_night', 'rating')
	model = Campground

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(CreateCampground, self).form_valid(form)

class CampgroundDetail(generic.DetailView):
	model = Campground

# add in get_query_set to filter by location
class CampgroundList(generic.ListView):
	model = Campground

class UpdateCampground(LoginRequiredMixin, generic.UpdateView):
	model = Campground
	fields = ('name', 'image', 'description')

	template_name_suffix = '_update_form'

class DeleteCampground(LoginRequiredMixin, generic.DeleteView):
	model = Campground
	success_url = reverse_lazy('campgrounds:all')
	
	def delete(self,*args, **kwargs):
		return super().delete(*args, **kwargs)

# Comment Views
class CreateReview(LoginRequiredMixin, generic.CreateView):
	fields = ('comment', 'rating')
	model = Review

	def form_valid(self, form):
		form.instance.author = self.request.user
		# form.instance.campground = self.request.
