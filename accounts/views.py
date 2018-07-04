from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.
class SignUp(CreateView):
	form_class = forms.UserCreateForm
	second_form_class = forms.UserProfileForm
	success_url = reverse_lazy('login')
	template_name = "accounts/signup.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form2'] = self.second_form_class()
		return context