from django.http import Http404
from django.template import TemplateDoesNotExist
#from django.views.generic.simple import direct_to_template
#from django.shortcuts import render_to_response, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from galleria.models import Tag, Image

# Creates list of images sorted by the tag-slug
def gal_by_tag(request, slug):
    r = request
	# Check to see if url = all
    if slug == 'all':
	    slug = {'name':'all', 'slug':'all'}
	    qs = Image.objects.order_by('-pub_date')  	        
    else:
		# Look up the tag slug (and raise a 404 if it can't be found).
    	slug = get_object_or_404(Tag, slug__iexact=slug)
        qs = Image.objects.filter(tags=slug)
    # Use the object list view for the heavy lifting.
    return list_detail.object_list(
        request,
        queryset = qs,
        template_name = 'galleria/image_list.html',
        template_object_name = 'image',
        extra_context = {"slug": slug, "tag_list" : Tag.objects.all()},
        paginate_by = 12,
            )

# Creates detail view of an image with bread_crumb back to the sorted image list
def image_detail(request, image_id):
    # Look up the Image (and raise a 404 if it's not found)
    image = get_object_or_404(Image, pk=image_id)
    r = request
    # Record the last accessed date
    #image.last_accessed = datetime.datetime.now()
    #image.save()

    # Show the detail page
    return list_detail.object_detail(
        request,
        queryset = Image.objects.all(),
        object_id = int(image_id),
		template_object_name = 'image',
        template_name = 'galleria/image_detail.html',
        extra_context = {"tag_list" : Tag.objects.filter(image=image_id)},          
    )

