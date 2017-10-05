from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^Contact$', views.contact, name='contact'),
    url(r'^send', views.send, name='send'),
    url(r'^sent', views.sent, name='sent'),
]
