from django.shortcuts import render
from django.views.generic import (
                                 ListView, 
                                 UpdateView, 
                                 TemplateView, 
                                 DeleteView, 
                                 DetailView,

                                )           
from django.views.generic.edit import CreateView
from .models import Posts
from django.urls import reverse_lazy

def LoadPage(request):
    return render(request, 'loadpage.html')

def ContactPage(request):
    return render(request, 'contact.html')

class HomePageView(ListView):
    model = Posts
    ordering = ["-created"]
    template_name = 'index.html'

class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts/post_detail.html'

class PostsPublicView(CreateView):
    model = Posts
    fields = ['photo', 'title', 'summary', 'content']
    template_name = 'posts/posts_create.html'

class PostsUpdateView(UpdateView):
    model = Posts
    fields = ['photo', 'title', 'summary', 'content']
    template_name = 'posts/post_update.html'


class PostsDeleteView(DeleteView):
    model = Posts
    success_url = reverse_lazy('home')
    template_name = 'posts/post_delete.html'

class ListPageView(ListView):
    model = Posts
    ordering = ["-created"]
    template_name = 'config/posts-list.html'

class PostsConfView(DetailView):
    model = Posts
    template_name = 'config/posts-conf.html'