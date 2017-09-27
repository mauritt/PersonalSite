from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<project_type>[A-z]+)/(?P<view>(Tile|List|tile|list))$', views.portfolio, name='portfolio'),
    url(r'^detail/(?P<project_id>[A-z 0-9]+)/$', views.detail, name='detail'),
]
