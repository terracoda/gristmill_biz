from django import template
from django.db import models
from homepage.models import Teaser

register = template.Library()
 
#note : Teaser.objects.all().order_by('order')
# The renderer, OrderedTeasersNode, fetches the homepage teasers     
class OrderedTeasersNode(template.Node):
    def render(self, context):
        context['teasers'] = Teaser.objects.all().order_by('order') 
        return ''
    
def get_teasers(parser, token):
    return OrderedTeasersNode()
get_teasers = register.tag(get_teasers)

# Usage in templates
# {% load get_teasers %}
# {% get_teasers %}
#  {% for teaser in teasers %}
#	 <li><a href="{{ teaser.link_url }}"><h2>{{ teaser.title }}</h2>
#       {% if teaser.image %}<img src="{{ teaser.image.get_img_url }}" 
#				title="teaser.image.title" alt="teaser.image.description" />
#	   {% endif %}  
#       <p>{{ teaser.blurb }}</p>
#	   </a></li>	 	 
#	{% endfor %}
