import django
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    url(r'^login/$', django.contrib.auth.views.login, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),
    url(r'^logout-then-login/$', django.contrib.auth.views.logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change/$', django.contrib.auth.views.password_change, name='password_change'),
    url(r'^password-change/done/$', django.contrib.auth.views.password_change_done, name='password_change_done'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
]
