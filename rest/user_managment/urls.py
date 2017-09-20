from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'new$', views.create_user, name='new_user'),
    url(r'(?P<user_id>[0-9]+)/edit$', views.edit_user, name='edit_user'),
    url(r'update$', views.update, name='update_user'),
    url(r'(?P<user_id>[0-9]+)$', views.show_user, name='show_user'),
    url(r'(?P<user_id>[0-9]+)/destroy$', views.destroy_user, name='destroy_user'),
    url(r'$', views.all_users, name='index'),
]