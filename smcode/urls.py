from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *

urlpatterns = [
    path('', views.LoadPage, name = 'loadpage'),
    path('contact/', views.ContactPage, name = 'contactpage'),
    path('code-idea/', HomePageView.as_view(), name = 'home'),
    path('posts/post/<int:pk>', PostsDetailView.as_view(), name = 'details'),
    path('posts/new-post', PostsPublicView.as_view(), name = 'post-new'),
    path('posts/delete/<int:pk>', PostsDeleteView.as_view(), name = 'post-delete'),
    path('posts/post/<int:pk>/edit', PostsUpdateView.as_view(), name = 'post-edit'),
    path('manage/posts/config', ListPageView.as_view(), name = 'lists'),
    path('manage/posts/config/<int:pk>', PostsConfView.as_view(), name = 'config'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
