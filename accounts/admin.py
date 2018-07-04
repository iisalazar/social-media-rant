from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserProfile)
class UserProfileInline(admin.TabularInline):
	model = models.UserProfile