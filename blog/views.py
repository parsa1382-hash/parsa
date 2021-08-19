from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def blog(request):
	posts = Post.objects.filter(status=1).order_by('-created_on')

	if not posts:
		posts = False

	return render(request, 'blog/blog.html', context={'posts': posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_detail.html', context = {'post': post})




# Create your views here.
