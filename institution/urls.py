from django.conf.urls import url
from .views import *
# 

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^p/(?P<article_id>[0-9]+)/$', detail,name='detail'),
    url(r'^report/$',report_view, name='report_view'),
    url(r'^createcompanyreport/$',createcompanyreport_view, name='createcompanyreport_view'),
    url(r'^companyinfo/(.+)/(.+)/change/$',report_companyinfo_view, name='report_companyinfo_view'),
    url(r'^save_reportback/$',save_reportback_view, name='save_reportback_view'),
    # url(r'^independentevaluationofenterprises_change/(\d+)/',IndependentEvaluationOfEnterprisesAdmin.change_view, name='independentevaluationofenterprises_change_view'),
]
