from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.views import generic
from campgrounds.models import Campground
# Create your views here.

class CreateCampground(LoginRequiredMixin, generic.CreateView):
	fields = ('name', 'image', 'description')
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



