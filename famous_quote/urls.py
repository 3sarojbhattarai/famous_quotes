from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from photos.views import PhotoView
from feedback.views import FeedbackView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', include('web.urls')),
    url(r'^photos/$', PhotoView.as_view(), name="home"),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
