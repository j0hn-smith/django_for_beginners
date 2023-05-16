from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "body"]


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "author", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:home")
