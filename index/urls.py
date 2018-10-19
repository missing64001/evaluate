from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),
    

    url(r'^admin/login/$',my_login, name='login'),
    url(r'',admin.site.urls),
    url(r'^register/$',register, name='register'),
    url(r'^logout/$',my_logout, name='my_logout'),
    url(r'^res/$',my_register, name='my_register'),

]