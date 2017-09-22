from . import views
from django.conf.urls import url, include

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^portfolio/(?P<project_type>[A-z]+)/$', views.portfolio, name='portfolio'),
]
