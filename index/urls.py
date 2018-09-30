from django.conf.urls import url
from .views import *


urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),
    url(r'^register/$',register, name='register'),
    url(r'^login/$',my_login, name='my_login'),
    url(r'^logout/$',my_logout, name='my_logout'),
    url(r'^admin/index/companyinfo/$',companyinfo_view, name='companyinfo_view'),
    url(r'^admin/index/financialsituation/$',financialsituation_view, name='financialsituation_view'),
    url(r'^admin/index/productsandmarket/$',productsandmarket_view, name='productsandmarket_view'),
    url(r'^admin/index/technologyrd/$',technologyrd_view, name='technologyrd_view'),
    url(r'^admin/index/serverrequest/$',serverrequest_view, name='serverrequest_view'),
    url(r'^admin/index/balance/$',balance_view, name='balance_view'),





]