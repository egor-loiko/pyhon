from django.urls import path, re_path
from . import views

app_name = 'addressbook'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.address, name='address')
]
