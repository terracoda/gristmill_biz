from galleria.models import Tag, Image

def get_recent_images(request):
    recent_images_list = Image.objects.order_by("-pub_date")[:8]  
    return {'IMAGE_LIST': recent_images_list}