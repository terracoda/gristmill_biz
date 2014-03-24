from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from galleria.models import Gallery

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Object List view
gallery_info = {
    "queryset" : Gallery.objects.all(),
}

urlpatterns = patterns('',
	(r'^gallery/$', list_detail.object_list, gallery_info),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),   
)
