from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class VideoPost(models.Model):
    title = models.CharField(max_length = 150)
    summary = models.CharField(max_length = 150)
    created = models.DateTimeField('data', auto_now_add = True, blank = True, null = True)
    content = models.TextField(null = True, blank = True)
    video = models.FileField(upload_to = 'videos/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_video_detail', args=[str(self.id)])

 
