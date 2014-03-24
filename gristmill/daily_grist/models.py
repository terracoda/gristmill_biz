from django.db import models
#from django.contrib.syndication.views.Feed import Feed
#from django.utils import feedgenerator
from django.contrib.sitemaps import Sitemap
import markdown
from taggit.managers import TaggableManager
from galleria.models import Image

import datetime

# Create your models here.
class Entry(models.Model):
	title = models.CharField(max_length=255)
	#Optional lead_image can be chosen from the photo gallery.
	lead_image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)
	slug = models.SlugField(unique_for_date='pub_date', help_text='Automatically created from the title.')
	body_html = models.TextField(blank=True)
	body_markdown = models.TextField(help_text='Use Markdown syntax')
	pub_date = models.DateTimeField('date published')
	mod_date = models.DateTimeField(auto_now=True) #defaults to now
	last_accessed = models.DateTimeField(auto_now=True) #defaults to now for a last accessed timestamp
	enable_comments = models.BooleanField(default=True)
	
	PUB_STATUS = (
	   (0, 'Draft'),
	   (1, 'Published'),
	)
	status = models.IntegerField(choices=PUB_STATUS, default=0)
	
	tags = TaggableManager()
	
	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = ('pub_date')
		verbose_name_plural = 'entries'
   	
	def __unicode__(self):
	    return u'%s' %(self.title)
	
	def get_absolute_url(self):
		return "/daily-grist/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
		     
	def save(self):
	    self.body_html = markdown.markdown(self.body_markdown, safe_mode=False)
	    super(Entry, self).save()
	
	def get_previous_published(self):
		return self.get_previous_by_pub_date(status__exact=1)
	
	def get_next_published(self):
		return self.get_next_by_pub_date(status__exact=1)

# taggit is not working	
#	def get_tags(self):
#		return Tag.objects.get_for_object(self)
		
