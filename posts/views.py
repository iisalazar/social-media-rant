from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Post, Comment
from . import forms
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import get_user_model 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.edit import FormMixin


# Create your views here.
User = get_user_model()

class PostList(LoginRequiredMixin, generic.ListView):
	model = Post

class UserPosts(generic.ListView):
	model = Post
	template_name = "posts/user_post_list.html"

	def get_queryset(self):
		try:
			self.post_user = User.objects.prefetch_related('posts').get(
				username__iexact=self.kwargs.get('username')
			)
		except User.DoesNotExist:
			raise Http404
		else:
			return self.post_user.posts.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_user'] = self.post_user
		return context
@login_required
def add_comment(request, username, pk):
	post = get_object_or_404(Post, pk=pk)
	user = get_object_or_404(User, username=username)
	if request.method == 'POST':
		form = forms.CommentCreateForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = user
			comment.save()
		else:
			print(form.errors)
	return redirect('posts:post_details', username=post.user.username, pk=post.pk)

class PostDetail(generic.DetailView, FormMixin):
	form_class = forms.CommentCreateForm
	model = Post
	success_url = reverse_lazy('home')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user__username__iexact=self.kwargs.get('username'))
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = forms.CommentCreateForm(initial={'post': self.object})
		return context


class CreatePost(LoginRequiredMixin, generic.CreateView):
	form_class = forms.PostCreateForm
	model = Post

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)

class DeletePost(LoginRequiredMixin, generic.DeleteView):
	model = Post
	success_url = reverse_lazy('home')
	pk_url_kwarg = "pk"

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user_id=self.request.user.id)

	def delete(self, *args, **kwargs):
		messages.success(request, "Successfully deleted post")
		return super().delete(*args, **kwargs)

