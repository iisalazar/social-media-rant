from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserCreateForm(UserCreationForm):
	class Meta:
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()

class UserProfileForm(forms.ModelForm):
	class Meta:
		fields = ('profile_picture',)
		model = models.UserProfile