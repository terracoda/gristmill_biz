from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.date_based import object_detail, archive_day, archive_month, archive_year, archive_index
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from galleria.models import Tag, Image
from galleria.views import gal_by_tag, image_detail 
from gristmill.views import HomeView, about_pages
from daily_grist.views import EntryListView, EntryDetailView
from testimonials.views import QuotationListView
from daily_grist.models import Entry
from testimonials.models import Quotation, Customer
from taggit.models import Tag, TaggedItem
import datetime

#from blog.models import Blog, Author, Entry
#from blog.views import news_blog_list, news_entry_detail

#info_dict for daily-grist
info_dict = {
    'date_field': 'pub_date',
    'queryset': Entry.objects.filter(status=1),
#    'allow_future': True,
#    'template_name': 'daily_grist/entry_archive.html',
#    'context_object_name': 'latest_entries',  
}      

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Come back to Home and About sections when galleria is done
# home
    (r'^$', HomeView.as_view()),
#
# About section
    (r'^about/$', direct_to_template, {'template': 'about/about.html'}),
    (r'^about/(\w+)/$', about_pages),
#
# Class-based Generic Views for galleria    
	(r'^tags/$', ListView.as_view(model=Tag, context_object_name="tag_list", template_name="tag_list.html",)),
#
# My own view functions for galleria
#    (r'^gallery/(all)/$', gal_all),														
    (r'^gallery/([\w-]+)/(?P<image_id>\d+)/$', image_detail),
    (r'^gallery/([\w-]+)/$', gal_by_tag),
#
# Class-based generic views for daily-grist
    (r'^daily-grist/archive/$', ArchiveIndexView.as_view(**info_dict),),
    (r'^daily-grist/$', EntryListView.as_view()),
    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', EntryDetailView.as_view(),),
#
# Class-based generic views for testimonials
    (r'^testimonials/$', QuotationListView.as_view()),
#
# Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#
#Daily-Grist urls
    #(r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', object_detail, dict(info_dict, slug_field='slug', template_object_name='entry', template_name='blog/entry_detail.html',)),
#    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', object_detail, dict(info_dict, template_object_name='entry_list', template_name='blog/entry_list.html',)),
#    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', archive_day,dict(info_dict, template_object_name='entry_list', template_name='blog/entry_list.html',)),
#    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',archive_month, dict(info_dict, template_object_name='entry_list', template_name='blog/entry_list.html',)),
#    (r'^daily-grist/(?P<year>\d{4})/$', archive_year, dict(info_dict, template_object_name='entry_list', template_name='blog/entry_list.html')),
    #(r'^daily-grist/$', archive_index, dict(info_dict, template_object_name='entry_list', template_name='blog/entry_list.html',)),
)    
#
# Will need to turn this off in production
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))