# The homepage views go here.

from django.views import generic
from django.shortcuts import get_object_or_404

from homepage.models import PageIntro, TeaserImage, Teaser

# Note: importing generic, so need to use dot notation when callig the classes

class HomepageView(generic.ListView):
	queryset = PageIntro.objects.filter(status=1) 
	template_name = 'homepage/index_list.html'
	context_object_name = 'page_intros'

# Note the homepage teasers are brought in through a template tag  