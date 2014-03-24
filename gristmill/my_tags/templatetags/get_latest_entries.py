#from django.template import Library, Node
#from django.db.models import get_model
from django import template
from django.db import models
from daily_grist.models import Entry

import datetime

register = template.Library()
 
#note : Entry.objects.filter(status=1).exclude(pub_date__gte=datetime.datetime.now())
# The renderer, LatestEntriesNode, fetches daily_grist blog entries     
class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.objects.filter(status=1).exclude(pub_date__gte=datetime.datetime.now())[:2]
        return ''
    
def get_latest_entries(parser, token):
    return LatestEntriesNode()
get_latest_entries = register.tag(get_latest_entries)

# Usage in templates is straightforward
# {% load get_latest_entries %} {% get_latest_entries %} and then loop over the entries