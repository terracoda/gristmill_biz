from django import template
from django.db.models import get_model

# Create the template tag library
register = template.Library()

# The renderer, LatestContentNode, fetches any kind of content    
class LatestContentNode(template.Node):
	def __init__(self, model, num, varname):
		self.num, self.varname = num, varname
		# the asterisk says take this list of things and use it as your arguments
		self.model = get_model(*model.split('.'))
		
	def render(self, context):
		context[self.varname] = self.model._default_manager.all()[:self.num]
		return ''

# The Compilation function
# Token is an argument given to every compilation function. 
# It's populated from the template tag, and in our case will be something like 
# 'get_lastest galleria.Image 5 as recent_images'   
def get_latest(parser, token):
	bits = token.contents.split()
	# the length of the split list must be 5
	if len(bits) != 5:
	    raise template.TemplateSyntaxError, "get_latest tag takes exactly four arguments"
	if bits[3] != 'as':
	        raise template.TemplateSyntaxError, "third argument to the get_latest tag must be 'as'"
	return LatestContentNode(bits[1], bits[2], bits[4])

# Registers the get_latest function as a tag
get_latest = register.tag(get_latest)

# Usage in templates
# {% load get_latest %} {% get_latest modelname.Objectname 5 as latest_objectname %}