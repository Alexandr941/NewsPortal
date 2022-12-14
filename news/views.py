from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = 'Post'
    ordering = 'title'
    queryset = Post.objects.order_by('dateCreation')
    template_name = 'news.html'
    context_object_name = 'Posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'