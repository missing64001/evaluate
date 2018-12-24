from django.conf.urls import url
from .views import *
from django.contrib import admin
# 

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),

    url(r'^companyinfo/$',companyinfo_view, name='companyinfo_view'),
    url(r'^financialsituation/$',financialsituation_view, name='financialsituation_view'),
    url(r'^productsandmarket/$',productsandmarket_view, name='productsandmarket_view'),
    url(r'^technologyrd/$',technologyrd_view, name='technologyrd_view'),
    url(r'^serverrequest/$',serverrequest_view, name='serverrequest_view'),
    url(r'^balance/(.+)/change/$',balance_view, name='balance_view'),
    url(r'^balance/submit_table/$',balance_submit_table_view, name='balance_submit_table_view'),
    url(r'^balance/add/$',balance_add_view, name='balance_add_view'),



    url(r'^profit/(.+)/change/$',profit_view, name='profit_view'),
    url(r'^profit/submit_table/$',profit_submit_table_view, name='profit_submit_table_view'),
    url(r'^profit/add/$',profit_add_view, name='profit_add_view'),

    url(r'^cashflow/(.+)/change/$',cash_flow_view, name='cash_flow_view'),
    url(r'^cashflow/submit_table/$',cash_flow_submit_table_view, name='cash_flow_submit_table_view'),
    url(r'^cashflow/add/$',cash_flow_add_view, name='cash_flow_add_view'),
    
    url(r'^deldata/$',deldata_view, name='deldata_view'),
    url(r'^independentevaluationofenterprises/(\d+)/',independentevaluationofenterprises_view, name='independentevaluationofenterprises_view'),
    url(r'^evaluationofenterprises/',evaluationofenterprises_to_independentevaluationofenterprises_view, name='evaluationofenterprises_to_independentevaluationofenterprises_view'),
    # url(r'^EvaluationOfEnterprises/(\d+)/',EvaluationOfEnterprisesview, name='EvaluationOfEnterprisesview'),

    
    url(r'^confirm/$',confirm_view, name='confirm_view'),
    url(r'^reject/$',reject_view, name='reject_view'),
    url(r'^verify/$',verify_view, name='verify_view'),
    # url(r'^independentevaluationofenterprises_change/(\d+)/',IndependentEvaluationOfEnterprisesAdmin.change_view, name='independentevaluationofenterprises_change_view'),



    url(r'^company_status/$',company_status_view, name='company_status_view'),



]
