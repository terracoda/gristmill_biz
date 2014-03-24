from django.db import models
from django import forms
#from django.contrib.sitemaps import Sitemap
import markdown
import datetime

# Models for the homepage application go here.
class PageIntro(models.Model):
	title = models.CharField(max_length=255)
	intro_text_html = models.TextField(blank=True)
	intro_text_markdown = models.TextField(help_text='Introduction paragraph(s). Use Markdown syntax' )
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	mod_date = models.DateTimeField('date modified',auto_now=True) #defaults to now
	
	PUB_STATUS = (
	   (0, 'Draft'),
	   (1, 'Published'),
	)
	status = models.IntegerField(choices=PUB_STATUS, default=0)

	class Meta:
		ordering = ('-pub_date',)
		verbose_name = 'homepage introduction'
		
	def __unicode__(self):
	    return u'%s' %(self.title)
    
	def save(self):
	    self.intro_text_html = markdown.markdown(self.intro_text_markdown, safe_mode=False)
	    super(PageIntro, self).save()
    
class TeaserImage(models.Model):
	name = models.ImageField(help_text='Width and height must be 220px by 105px. Images are uploaded to the teasers folder.', upload_to='teasers/')
	title = models.CharField(help_text='Optional: title attribute text (shows on mouse-over) (maximum length 100 characters)', max_length=100, null=True, blank=True) 
	description = models.CharField(help_text='Required: image description for alt attributes (maximum length 100 characters)', max_length=100)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
    
	class Meta:
		ordering = ['name']
	
	def __unicode__(self):
		return u'%s' %(self.name)
	
	""" Wrapper function to use in template to get the path to the image file. """
	def get_img_url(self):
		return "/media/%s" %(self.name)
   
class Teaser(models.Model):
	link_url = models.CharField(max_length=100, help_text='URL or URI to the content, eg /about/ or http://foo.com/')                        
	title = models.CharField(help_text='Teaser title (maximum length 50 characters)', max_length=50)
	blurb = models.TextField(help_text='Teaser text blurb (maximum length 100 characters)', max_length=100)
	image = models.ForeignKey(TeaserImage)
	pub_date = models.DateTimeField('date published')
	mod_date = models.DateTimeField(auto_now=True) #defaults to now
	order = models.PositiveIntegerField(help_text='Tip: use multiples of 10, so it is easy to change the order.', max_length=1000)

	class Meta:
		ordering = ('order','-pub_date', 'title')

	def __unicode__(self):
	    return "%s %s. %s %s" % (self.title, self.order, self.link_url, self.image.name)   