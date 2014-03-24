from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
#from django.views.generic.date_based import object_detail, archive_day, archive_month, archive_year, archive_index
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from galleria.models import Tag, Image
from galleria.views import gal_by_tag, image_detail 
from gristmill.views import HomeStaticTemplateView, about_pages
from daily_grist.views import EntryListView, EntryDetailView, BlogArchiveIndexView
from testimonials.views import QuotationListView
from testimonials.views import TestimonialArchiveIndexView
from homepage.views import HomepageView
from daily_grist.models import Entry
from testimonials.models import Quotation, Customer
from homepage.models import PageIntro, TeaserImage, Teaser
from contact.forms import ContactForm
from contact.views import contact

# from taggit.models import Tag, TaggedItem
import datetime      

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Come back to Home and About sections when galleria is done
# home
    (r'^$', HomepageView.as_view()),
#
# Class-based Generic Views for galleria    
	(r'^tags/$', ListView.as_view(model=Tag, context_object_name="tag_list", template_name="galleria/tag_list.html",)),
#
# My own view functions for galleria
#    (r'^gallery/(all)/$', gal_all),														
    #(r'^gallery/([\w-]+)/(?P<image_id>\d+)/$', image_detail),
    (r'^gallery/(\d+)/$', image_detail),
    (r'^gallery/([\w-]+)/$', gal_by_tag),
#
# Class-based generic views for daily-grist
    (r'^daily-grist/$', EntryListView.as_view()),
    (r'^daily-grist/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w-]+)/$', EntryDetailView.as_view(),),
    (r'^daily-grist/archive/$', BlogArchiveIndexView.as_view(),),
    #(r'^daily-grist/archive/(?P<year>\d{4})/$', BlogYearArchiveView.as_view(),),
#
# Class-based generic views for testimonials
    (r'^testimonials/$', QuotationListView.as_view()),
	(r'^testimonials/archive/$', TestimonialArchiveIndexView.as_view()),
#
# Forms
    (r'^contact/$', contact),
    (r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),

#
# All content subsections are flatpages
    #(r'^about/$', direct_to_template, {'template': 'about/about.html'}),
    #(r'^about/(\w+)/$', about_pages),
#
# Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)    
#
# Will need to turn this off in production
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))