"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 
        'django.views.generic.list_detail.object_list',
        {
            'queryset': Article.published.all(),
        },
        name='wiki_article_index'),
    url(r'^article/(?P<slug>[-\w]+)$', 
        'django.views.generic.list_detail.object_detail',
        {
            'queryset': Article.objects.all(),
        },
        name='wiki_article_detail'),
    url(r'^history/(?P<slug>[-\w]+)$', 'wiki.views.article_history', name='wiki_article_history'),
    url(r'^add/article$', 'wiki.views.add_article', name='wiki_article_add'),
    url(r'^edit/article/(?P<slug>[-\w]+)$', 'wiki.views.edit_article', name='wiki_article_edit'),
]
