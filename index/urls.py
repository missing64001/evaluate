from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),
    

    url(r'',admin.site.urls),
    url(r'^register/$',register, name='register'),
    url(r'^login/$',my_login, name='my_login'),
    url(r'^logout/$',my_logout, name='my_logout'),
    url(r'^admin/index/companyinfo/$',companyinfo_view, name='companyinfo_view'),
    url(r'^admin/index/financialsituation/$',financialsituation_view, name='financialsituation_view'),
    url(r'^admin/index/productsandmarket/$',productsandmarket_view, name='productsandmarket_view'),
    url(r'^admin/index/technologyrd/$',technologyrd_view, name='technologyrd_view'),
    url(r'^admin/index/serverrequest/$',serverrequest_view, name='serverrequest_view'),
    url(r'^admin/index/balance/$',balance_view, name='balance_view'),
    url(r'^admin/index/balance/submit_table/$',balance_submit_table_view, name='balance_submit_table_view'),



    url(r'^admin/index/profit/$',profit_view, name='profit_view'),
    url(r'^admin/index/profit/submit_table/$',profit_submit_table_view, name='profit_submit_table_view'),
    url(r'^admin/index/cash_flow/$',cash_flow_view, name='cash_flow_view'),
    url(r'^admin/index/cash_flow/submit_table/$',cash_flow_submit_table_view, name='cash_flow_submit_table_view'),


]