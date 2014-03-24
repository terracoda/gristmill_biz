from django.contrib import admin
from galleria.models import Tag, Image
from galleria.admin import TagAdmin, ImageAdmin
from daily_grist.models import Entry
from daily_grist.admin import EntryAdmin
from testimonials.models import Customer, Quotation
from testimonials.admin import CustomerAdmin, QuotationAdmin

class AdminSite(admin.AdminSite):
	pass

site = AdminSite()
site.register(Tag, Image, TagAdmin, ImageAdmin, Entry, EntryAdmin, Customer, Quotation, CustomerAdmin, QuotationAdmin)