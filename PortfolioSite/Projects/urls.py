from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<project_type>[A-z]+)$', views.portfolio, name='portfolio'),
    url(r'^(?P<project_type>[A-z]+)/tag/(?P<project_tag>[A-z]+)/(?P<view>(Tile|List|tile|list))$', views.tag, name='tag'),
    url(r'^details/(?P<project_id>[A-z 0-9]+)/$', views.detail, name='detail'),
]
