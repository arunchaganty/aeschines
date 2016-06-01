from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/((?P<entity>[HCDTBS]{2})/)?((?P<stance>[01+-]+)/)?((?P<topic>[a-zA-Z &]+)/)?$', views.view_tweets),
    url(r'^summary/$', views.summary),
]
