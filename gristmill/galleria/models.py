from django.db import models
from django.db.models import permalink

class Tag(models.Model):
	name = models.CharField('tag name', help_text='maximum length 100', max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True, help_text='Suggested value automatically created from name. Must be unique.') 
	def __unicode__(self):
		return u"%s" % (self.name)

	class Meta:
		ordering = ['name']
    
	"""
	Permanent url to a tag's slug. Can be used in templates."""
	@permalink
	def get_absolute_url(self):
		return ('galleria.views.gal_by_tag', [str(self.slug)])
   	
class Image(models.Model):
    filename = models.ImageField(help_text='Width and height no larger than 700px at 72dpi. Images are uploaded to the photos folder. Duplicates will have a an underscore and number added to filename (eg. image_2.jpg)', upload_to='photos/')
    caption = models.CharField(help_text='Short catchy title for the image (maximum length 100 characters)', max_length=100)
    description = models.TextField(help_text='Longer description of the image. Try to build some interest here, keep it to under 300 characters.', max_length=300, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag)
#	enable_comments = 
    def __unicode__(self):
		return u"%s (%s)" % (self.caption, u", ".join([tag.name
		                                            for tag in self.tags.all()]))
    class Meta:
		ordering = ['-pub_date']		

    """
    Permanent url to image detail view to use in templates."""
    @permalink
    def get_absolute_url(self):
	    return ('galleria.views.image_detail', [str(self.id)])
	
    """
	Wrapper function to use in template to get the path to the image file. """
    def get_img_url(self):
        return "/media/%s" %(self.filename)
