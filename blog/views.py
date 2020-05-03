from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'blog/index.html'
    paginate_by = 3

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'
