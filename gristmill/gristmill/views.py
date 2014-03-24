from django.http import Http404
from django.template import TemplateDoesNotExist
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.views import generic
#from django.views.generic import TemplateView, list_detail, DetailView, ListView
from django.views.generic.list_detail import object_list
from galleria.models import Image

#from daily_grist.models import Entry
#from testimonials.models import Quotation, Customer

import datetime

class HomeStaticTemplateView(generic.TemplateView):
	template_name = 'index_static.html'

# Dynamic urls for the About section
# If a template doesn't exist, a 404 is raised
def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()

# Class-based generic views example
#class AboutView(TemplateView):
#    template_name = "path/to/template/name_of_template.html" 


#class HomeView(ListView):
#
#    context_object_name = "content_list"
#    queryset = Entry.objects.order_by("-pub_date")[:3]
#    template_name = 'home_extras.html'
#
#    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
#        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images        
        #context['testimonial'] = Quotation.objects.get(id=1)
        #context['entry_list'] = Entry.objects.order_by("-pub_date")[:1]
        #context['image_list'] = Image.objects.order_by("-pub_date")[:11]
#        return context	
	
                  
#def home_view(request):
	#todo - page_content will be something else eventually.
#    page_content = Entry.objects.order_by("-pub_date")[:3]
    #random_testimonial = Quotation.objects.get(id=1)
    #recent_news_list = Entry.objects.order_by("-pub_date")[:2]
    #recent_images_list = Image.objects.order_by("-pub_date")[:11]
   
#    return object_list(request, 
#        queryset = page_content,
#        template_object_name = 'content', 
        #extra_context={'testimonial': random_testimonial, 'entry_list': recent_news_list, 'image_list': recent_images_list},
#        template_name='home_extras.html',)

