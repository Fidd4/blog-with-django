from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from ourblog import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
