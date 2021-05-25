from .views import SongUploaderView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

music = SongUploaderView.as_view({
    'get': 'list',
    'post': 'create'
})
music1 = SongUploaderView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch':'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('songs_api/', music),
    path('songs_api/<int:pk>', music1),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)