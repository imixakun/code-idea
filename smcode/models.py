from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField('title', max_length = 150)
    summary = models.CharField('summary', max_length = 150)
    created = models.DateTimeField('data', auto_now_add = True, blank = True, null = True)
    photo = models.ImageField('image', upload_to = 'photos/')
    content = models.TextField('content', blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
