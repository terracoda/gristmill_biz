#daily_grist urls
from django.conf.urls.defaults import *
from daily_grist.models import Entry
import datetime

info_dict = {
    'date_field': 'pub_date',
    'queryset': Entry.objects.exclude(pub_date__gte=datetime.now()).filter(status=1),
}

urlpatterns = patterns('django.generic.views.date_based',
    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', 'object_detail', dict(info_dict, slug_field='slug',template_name='blog/detail.html')),
    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', 'object_detail', dict(info_dict, template_name='blog/list.html')),
    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', 'archive_day',dict(info_dict,template_name='blog/list.html')),
    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(info_dict, template_name='blog/list.html')),
    (r'^daily-grist/(?P<year>\d{4})/$','archive_year', dict(info_dict, template_name='blog/list.html')),
    (r'^daily-grist/$','archive_index', dict(info_dict, template_name='blog/list.html')),   
)