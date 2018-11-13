from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),

    url(r'^admin/$',MyAdminIndex, name='index'),
    url(r'^admin/login/$',my_login, name='login'),
    url(r'^admin/staff/$',my_staff, name='my_staff'),
    url(r'',admin.site.urls),
    # url(r'^register/$',register, name='register'),
    url(r'^logout/$',my_logout, name='my_logout'),
    url(r'^res/$',my_register, name='my_register'),
    url(r'^savedata/$',savedata_view, name='savedata_view'),


]