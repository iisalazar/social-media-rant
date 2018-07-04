from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
	path('new', views.CreatePost.as_view(), name="create_post"),
	path('by/<username>/', views.UserPosts.as_view(), name="user_posts"),
	path('by/<username>/<int:pk>/', views.PostDetail.as_view(), name="post_details"),
	path('delete/<int:pk>', views.DeletePost.as_view(), name="delete_post"),
	path('add_comment/<username>/<int:pk>/', views.add_comment, name="add_comment")
]