from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=100, help_text="Use 'anonymous', if name not known.")
	city = models.CharField(max_length=100, null=True, blank=True)
	state_province = models.CharField(verbose_name="State/Province", max_length=5, help_text="Please use valid abbreviations.", null=True, blank=True)
   # country = models.CharField(max_length=5, help_text="Please use valid abbreviations.", null=True, blank=True)
	
	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return u"%s" % (self.name)


#Choices list for quotation status. The default is 'Keep private'.
PUB_STATUS = (
    (0, 'Keep private'),
    (1, 'Make public'),
)   

class Quotation(models.Model):
    quote = models.TextField(max_length=1000)
    date = models.DateField(verbose_name="quotation date", help_text="Date format is YYYY-MM-DD. You can use the calendar icon. If unknown, use the Today link.") 
    mod_date = models.DateTimeField(auto_now=True) #should default to now for a timestamp
    customer = models.ForeignKey(Customer)
    status = models.IntegerField(choices=PUB_STATUS, default=0, help_text="Choose 'Make public'. Defaults to 'Keep private'.")

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __unicode__(self):
        return u"%s" % (self.quote)

    def get_absolute_url(self):
        return "/%s/%s/" %(self.date.strftime("%Y/%b/%d").str(), self.id)