#from django.template import Library, Node
#from django.db.models import get_model
from django import template
from django.db import models
from testimonials.models import Quotation


register = template.Library()
 
#note : Quotation.objects.order_by('?')
# The renderer, RandomQuotationNode, fetches a randomly selected quotation     
class RandomQuotationNode(template.Node):
    def render(self, context):
        context['quotation'] = Quotation.objects.order_by('?')[0]
        return ''
    
def get_random_quotation(parser, token):
    return RandomQuotationNode()
get_random_quotation = register.tag(get_random_quotation)

# Usage in templates is straightforward
# {% load get_random_testimonial %}
# {% get_random_quotation %}
# <blockquote>{{ quotation.quote }}</blockquote>   				
# 	<p class="citation">
# 		<em class="quoteSource">{{ quotation.customer }}</em> <br>
# 		<span class="place">{{ quotation.customer.city }}, {{ quotation.customer.state_province }}</span><br>
# 	   <span class="date">{{ quotation.date }}</span> 
# 	 </p>