# Create your views here.
#from django.http import HttpResponse
#from django.shortcuts import render_to_response, get_object_or_404
#from galleria.models import Image, Gallery, Tag
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

#def index(request):
#	lastest_images_list = Image.objects.images.all().order_by('-pub_date')[:5]
#	output = 
#    return HttpResponse("Hello, world. You're at the galleria index.")
#def gallery_index(request):
#	return HttpResponse("You are looking at the gallery index.")
#	
#def gallery_detail(request, gallery_id):
#	return HttpResponse("You are looking at the gallery %s." % gallery_id)
#
#def gallery_detail(request, gallery_id):
#    g = get_object_or_404(Gallery, pk=gallery_id)
#    return render_to_response('galleria/gallery.html', {'gallery': g})
#return HttpResponseRedirect(reverse('image_details', args=(p.id,)))
def gallery_pages(request, page):
    try:
        return direct_to_template(request, template="galleria/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()
