from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ( VideoPostCreateView,
                     VideoPostUpdateView,
                     VideoPostDetailView,
                     VideoPostDeleteView,
                     VideoListView,
                     VideoPageView,
                     VideoConfDetailView,
                    )

urlpatterns = [
    path('', VideoListView.as_view(), name = 'video_list'),
    path('post/vlay/new/', VideoPostCreateView.as_view(), name = 'post_video_new'),
    path('post/vlay/<int:pk>/', VideoPostDetailView.as_view(), name = 'post_video_detail'),
    path('post/vlay/<int:pk>/update/', VideoPostUpdateView.as_view(), name = 'post_video_edit'),
    path('post/vlay/<int:pk>/delete/', VideoPostDeleteView.as_view(), name = 'post_video_delete'),
    path('manage/vlay/', VideoPageView.as_view(), name = 'conf-list'),
    path('manage/vlay/<int:pk>/', VideoConfDetailView.as_view(), name = 'conf-detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )