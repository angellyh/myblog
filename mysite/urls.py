"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/',include('grappelli.urls')),
    (r'^comments/', include('django_comments.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', views.default),
    (r'^base/$', views.r_sidebar),
    (r'^blog/$', views.default),
    (r'^article/$', views.article_detail),
    (r'^article-list/$', views.article_list),
    (r'^aboutme/$', views.about_me),
    (r'^themes/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': 'D:\myweb\mysite/blog/templates'}),
    )
urlpatterns += staticfiles_urlpatterns() 