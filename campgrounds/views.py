from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.views import generic
from campgrounds.models import Campground,Review
from .forms import ReviewForm
from django.db.models import Avg


# Campground Views
class CreateCampground(LoginRequiredMixin, generic.CreateView):
	fields = ('name', 'image', 'short_description', 'price_per_night', 'city', 'province')
	model = Campground

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(CreateCampground, self).form_valid(form)

class CampgroundDetail(generic.DetailView):
	model = Campground

	def get_context_data(self, **kwargs):
		context = super(CampgroundDetail, self).get_context_data(**kwargs)
		context['rating'] = self.object.reviews.aggregate(Avg('rating'))
		return context

# add in get_query_set to filter by location
class CampgroundList(generic.ListView):
	model = Campground

class UpdateCampground(LoginRequiredMixin, generic.UpdateView):
	model = Campground
	fields = ('name', 'image', 'short_description', 'price_per_night', 'city', 'province')

	template_name_suffix = '_update_form'

class DeleteCampground(LoginRequiredMixin, generic.DeleteView):
	model = Campground
	success_url = reverse_lazy('campgrounds:all')
	
	def delete(self,*args, **kwargs):
		return super().delete(*args, **kwargs)


# Comment Views
@login_required
def add_review_to_campground(request, pk): 
	campground = get_object_or_404(Campground, pk=pk)

	if request.method == 'POST':
		form = ReviewForm(request.POST)

		if form.is_valid():
			review = form.save(commit=False)
			review.campground = campground
			review.author = request.user
			review.save()
			return redirect('campgrounds:details', pk=campground.pk)
	else:
		form = ReviewForm()

	return render(request, 'campgrounds/review_form.html', {'form':form})

class UpdateReview(LoginRequiredMixin, generic.UpdateView):
	model = Review
	fields = ('comment', 'rating')

	template_name_suffix = '_update_form'

class DeleteReview(LoginRequiredMixin, generic.DeleteView):
	model = Review
	success_url = reverse_lazy('campgrounds:all')

	def delete(self, *args, **kwargs):
		return super().delete(*args, **kwargs)


	


