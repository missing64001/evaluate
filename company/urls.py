from django.conf.urls import url
from .views import *
from django.contrib import admin
# 

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),
    url(r'^companyinfo_opt/$',companyinfo_view, name='companyinfo_view'),
    url(r'^financialsituation/$',financialsituation_view, name='financialsituation_view'),
    url(r'^productsandmarket/$',productsandmarket_view, name='productsandmarket_view'),
    url(r'^technologyrd/$',technologyrd_view, name='technologyrd_view'),
    url(r'^serverrequest/$',serverrequest_view, name='serverrequest_view'),
    url(r'^balance/$',balance_view, name='balance_view'),
    url(r'^balance/submit_table/$',balance_submit_table_view, name='balance_submit_table_view'),



    url(r'^profit/$',profit_view, name='profit_view'),
    url(r'^profit/submit_table/$',profit_submit_table_view, name='profit_submit_table_view'),
    url(r'^cash_flow/$',cash_flow_view, name='cash_flow_view'),
    url(r'^cash_flow/submit_table/$',cash_flow_submit_table_view, name='cash_flow_submit_table_view'),
    url(r'^independentevaluationofenterprises/(\d+)/',independentevaluationofenterprises_view, name='independentevaluationofenterprises_view'),
    # url(r'^independentevaluationofenterprises_change/(\d+)/',IndependentEvaluationOfEnterprisesAdmin.change_view, name='independentevaluationofenterprises_change_view'),
]