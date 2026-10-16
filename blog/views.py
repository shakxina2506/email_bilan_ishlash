from django.shortcuts import render

from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,DetailView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    form_class = PostForm
    template_name = 'blog/post_detail.html'
    pk_url_kwarg = 'pk'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_list')

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('post_list')