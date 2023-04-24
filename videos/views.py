from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DetailView, DeleteView, ListView, TemplateView
from django.urls import reverse_lazy


class VideoListView(ListView):
    model = VideoPost
    ordering = ['-created']
    template_name = 'video_list.html'
    
class VideoPostCreateView(CreateView):
    model = VideoPost
    fields = ['title', 'video', 'summary', 'content']
    template_name = 'video/post_new.html'

class VideoPostUpdateView(UpdateView):
    model = VideoPost
    fields = ['title', 'video', 'summary', 'content']
    template_name = 'video/post_edit.html'

class VideoPostDetailView(DetailView):
    model = VideoPost
    template_name = 'video/post_detail.html'

class VideoPostDeleteView(DeleteView):
    model = VideoPost
    template_name = 'video/post-delete.html'
    success_url = reverse_lazy('home')

class VideoPageView(ListView):
    model = VideoPost
    ordering = ["-created"]
    template_name = 'vconfig/posts-list.html'

class VideoConfDetailView(DetailView):
    model = VideoPost
    template_name = 'vconfig/posts-conf.html'


