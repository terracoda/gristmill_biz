# The Daily Grist Blog views go here.

from django.views import generic
from django.shortcuts import get_object_or_404
from testimonials.models import Quotation, Customer

import datetime

# Note: importing generic, so need to use dot notation when callig the classes

class QuotationListView(generic.ListView):
	template_name = 'testimonals/quotation_list.html'
	paginate_by = 4 #15 is the default
	context_object_name = 'quotation_list'
	
	#Note: must filter on status to show only published testimonials.
	def get_queryset(self):
		return Quotation.objects.filter(status=1).order_by('-date')

# ArchiveIndexView
class TestimonialArchiveIndexView(generic.ArchiveIndexView):
	# allow_empty = False
	# allow_future = False
	date_field = 'date'
	#  http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace'] 
	context_object_name = 'latest_quotations' # default latest
	model = Quotation
	paginate_by = 4 # default is 15 
	queryset = Quotation.objects.filter(status=1).order_by('customer').order_by('date')
	template_name = 'testimonial/quotation_archive.html'
	# template_name_suffix = '_archive'
   
	