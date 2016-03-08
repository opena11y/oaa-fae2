"""
Copyright 2014-2016 University of Illinois

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# reports/urls.py
from django.conf.urls import url
from .views import RunReportView
from .views import RunAnonymousReportView
from .views import RunRefererReportView

from .views import ProcessingAnonymousReportView
from .views import ProcessingReportView

from .views import ArchivedReportView
from .views import ManageReportView

from .views import ProcessingStatusJSON
from .views import ProcessingStatusAllJSON
from .views import SetReportArchiveView

from .views import URLInformationView

from .views import ReportRulesView
from .views import ReportRulesGroupView
from .views import ReportRulesGroupRuleView
from .views import ReportRulesGroupRulePageView

from .views import ReportPagesView
from .views import ReportPagesGroupView

from .views import ReportPageView
from .views import ReportPageGroupView
from .views import ReportPageGroupRuleView

from fae2.settings import ANONYMOUS_ENABLED
from fae2.settings import SELF_REGISTRATION_ENABLED
from fae2.settings import SHIBBOLETH_ENABLED

urlpatterns = [
    url(r'^$',                RunReportView.as_view(),         name='run_report'),
    url(r'^processing/$',     ProcessingReportView.as_view(),  name='processing_reports'),
    url(r'^evaluate/link/$',  RunRefererReportView.as_view(),  name='run_referer_report'),
 
    url(r'^processing/status/all/$',              ProcessingStatusAllJSON.as_view(), name='processing_status_all'),
    url(r'^processing/status/(?P<report>\w+)/$',  ProcessingStatusJSON.as_view(),    name='processing_status'),
    url(r'^set-report-archive/(?P<report>\w+)/(?P<value>\w+)/$',   SetReportArchiveView.as_view(),       name='set_report_archive'),


    url(r'^archived/$',              ArchivedReportView.as_view(),     name='archived_reports'),
    url(r'^manage/$',                ManageReportView.as_view(),       name='manage_reports'),

    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/urls/$',                                                    URLInformationView.as_view(),  name='report_url_information'),

    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/$',                                                         ReportRulesView.as_view(),              name='report_rules'),
    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/(?P<group>\w+)/$',                                          ReportRulesGroupView.as_view(),         name='report_rules_group'),
    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/(?P<group>\w+)/rule/(?P<rule>\w+)/$',                       ReportRulesGroupRuleView.as_view(),     name='report_rules_group_rule'),
    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/(?P<group>\w+)/rule/(?P<rule>\w+)/page/(?P<page>[\d-]+)/$', ReportRulesGroupRulePageView.as_view(), name='report_rules_group_rule_page'),

    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/pages/all$',                                            ReportPagesView.as_view(),           name='report_pages'),
    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/pages/(?P<group>\w+)/$',                                ReportPagesGroupView.as_view(),      name='report_pages_group'),

    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/page/(?P<page>[\d-]+)/$',                               ReportPageView.as_view(),           name='report_page'),
    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/page/(?P<page>[\d-]+)/(?P<group>\w+)/$',                ReportPageGroupView.as_view(),      name='report_page_group'),
    url(r'^report/(?P<report>\w+)/(?P<view>\w+)/page/(?P<page>[\d-]+)/(?P<group>\w+)/(?P<rule>\w+)/$',  ReportPageGroupRuleView.as_view(),  name='report_page_group_rule'),
]

if ANONYMOUS_ENABLED:
  urlpatterns += [
    url(r'^anonymous/$',             RunAnonymousReportView.as_view(),        name='run_anonymous_report'),
    url(r'^anonymous/processing/$',  ProcessingAnonymousReportView.as_view(), name='processing_anonymous_reports'),
  ]