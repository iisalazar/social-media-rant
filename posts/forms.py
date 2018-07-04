from django import forms
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('message', 'tag')

		widgets = {
			'message': forms.Textarea()
		}

class CommentCreateForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('message',)
		widgets = {
			'message': forms.TextInput(attrs={'placeholder': 'say something'})
		}