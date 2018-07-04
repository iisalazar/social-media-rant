from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
User = get_user_model()
class Post(models.Model):
	tag_choice = (
		("Rant/Story", "Rant/Story"),
		("Question", "Question"),
		("Collaboration", "Collaboration")
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
	created_date = models.DateTimeField(auto_now=True)
	message = models.TextField()
	tag = models.CharField(max_length=100, choices=tag_choice, null=False)

	def get_absolute_url(self):
		return reverse('home')

	def __str__(self):
		return self.user.username + ": " + self.message

	class Meta:
		ordering = ['-created_date']
		unique_together = ['user', 'message']

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments", blank=True, null=True)
	message = models.TextField()
	date_created = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'username': post.user.username, 'pk': self.post.pk})

	def __str__(self):
		return self.message

	class Meta:
		ordering = ['date_created']
		unique_together = ['user', 'post', 'message']