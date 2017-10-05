from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from . import forms
from .models import User

# Create your views here.
class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'

class AccountDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
	model = User
