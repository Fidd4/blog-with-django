from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^post/add-post/$', views.add_post, name='add-post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostUpdate.as_view(), name='update-post'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.PostDelete.as_view(), name='delete-post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post-detail'),

    url(r'^tag/add-tag/$', views.add_tag, name='add-tag'),
    url(r'^tag/(?P<slug>[-\w]+)/edit/$', views.TagUpdate.as_view(), name='update-tag'),
    url(r'^tag/(?P<slug>[-\w]+)/remove/$', views.TagDelete.as_view(), name='delete-tag'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.TagDetail.as_view(), name='tag-detail'),
]
