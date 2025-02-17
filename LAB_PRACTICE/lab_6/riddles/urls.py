from django.urls import path, re_path
from . import views

# новые import для API
from django.conf.urls import include
from riddles.api import RiddleResource, OptionResource
from tastypie.api import Api

# api_name будет указываться в URLах
# перед resource_name из api.py
api = Api(api_name='api')
api.register(RiddleResource())
api.register(OptionResource())


app_name = 'riddles'
urlpatterns = [
    path(r'', views.index, name='index'),
    re_path(r'^([0-9]+)/$', views.detail, name='detail'),
    re_path(r'^([0-9]+)/answer/$', views.answer, name='answer'),
    re_path(r'^register/$', views.RegisterFormView.as_view()),
    re_path(r'^login/$', views.LoginFormView.as_view()),
    re_path(r'^logout/$', views.LogoutView.as_view()),
    re_path(r'^password-change/', views.PasswordChangeView.as_view()),
# отправка сообщения
    re_path(r'^([0-9]+)/post/$', views.post, name='post'),
# отправка списка сообщений
    re_path(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),
# отправка оценки
    re_path(r'^([0-9]+)/post_mark/$', views.post_mark, name='post_mark'),
# средняя оценка
    re_path(r'^([0-9]+)/get_mark/$', views.get_mark, name='get_mark'),
    re_path(r'^admin/$', views.admin, name='admin'),
    re_path(r'^post_riddle/$', views.post_riddle, name='post_riddle'),
    re_path(r'^subscribe/$', views.SubscribeView.as_view()),
    re_path(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
# для API
    re_path(r'^', include(api.urls)),

]

