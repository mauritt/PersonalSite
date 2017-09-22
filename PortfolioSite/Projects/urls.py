from . import views
from django.conf.urls import url, include

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^portfolio/(?P<project_type>[A-z]+)/$', views.portfolio, name='portfolio'),
    url(r'^portfolio/detail/(?P<project_id>[A-z 0-9]+)/$', views.detail, name='detail'),
]
