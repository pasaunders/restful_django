from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.),
    url(r'^new$', views.),
    url(r'^(?P<user_id>)/edit$', views.),
    url(r'^(?P<user_id>)$', views.),
    url(r'^create$', views.),
    url(r'^(?P<user_id>)/destroy$', views.),
]