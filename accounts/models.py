from django.db import models

from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
	
	def __str__(self):
		return "@{}".format(self.username)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	profile_picture = models.ImageField(blank=False, upload_to='profile_picture')

	def __str__(self):
		return self.profile_picture