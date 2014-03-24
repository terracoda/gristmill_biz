# The Daily Grist Blog views go here.

from django.views import generic
from django.shortcuts import get_object_or_404
#from django.views.generic.dates import dates

from daily_grist.models import Entry

import datetime

# Note: importing generic, so need to use dot notation when callig the classes

class EntryListView(generic.ListView):
	template_name = 'daily_grist/entry_list.html'
	paginate_by = 3
	context_object_name = 'entries'
	
	#Note: must filter on status to prevent publishing drafts and future articles. This works on the blog index page.
	def get_queryset(self):
		return Entry.objects.filter(status=1).exclude(pub_date__gte=datetime.datetime.now())
	
class EntryDetailView(generic.DetailView):
    # Use the Entry model
    model = Entry  #shorthand for queryset = Entry.objects.all()

	# Template to render
    template_name = 'daily_grist/entry_detail.html'
	
	# Defines the context name in the template
    context_object_name = 'entry' 
    
    #Tip: remember how to refer to kwargs: self.kwargs['slug']
    def get_object(self, **kwargs):
	    slug_field = super(EntryDetailView, self).get_slug_field(**kwargs)
	    return get_object_or_404(Entry, slug__iexact=self.kwargs['slug'])

    
# ArchiveIndexView
class BlogArchiveIndexView(generic.ArchiveIndexView):
	# allow_empty = False
	# allow_future = False
	date_field = 'pub_date'
	#  http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace'] 
	context_object_name = 'latest_entries' # default latest
	model = Entry
	paginate_by = 10 # default is 15 
	queryset = Entry.objects.filter(status=1)
	template_name = 'daily_grist/entry_archive.html'
	# template_name_suffix = '_archive'
 
# Todo: Make proper dated archive later.
#class BlogYearArchiveView(generic.YearArchiveView):
#	# allow_empty = False
#	# allow_future = False
#	context_object_name = 'entry_list' # default None
#	date_field = 'pub_date'
#	#  http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']
#	make_object_list = True
#	model = Entry
#	#paginate_by = None # default is None 
#	queryset = Entry.objects.filter(status=1)
#	template_name = 'daily_grist/entry_archive_year.html'
#	# template_name_suffix = '_archive_year'
#	# year = None
#	year_format ='%Y'	


		
	
     