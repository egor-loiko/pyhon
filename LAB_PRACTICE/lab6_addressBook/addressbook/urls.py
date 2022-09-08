from django.urls import path, re_path
from . import views

app_name = 'addressbook'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.address, name='address'),
    re_path(r'^register/$', views.RegisterFormView.as_view()),
    re_path(r'^login/$', views.LoginFormView.as_view()),
    re_path(r'^logout/$', views.LogoutView.as_view()),
    re_path(r'^password-change/', views.PasswordChangeView.as_view()),
# отправка сообщения
    re_path(r'^([0-9]+)/post/$', views.post, name='post'),
# отправка списка сообщений
    re_path(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),


]
