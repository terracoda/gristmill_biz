from django.contrib import admin
from testimonials.models import Customer, Quotation

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ["name"]

class QuotationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'quote', 'date',)
    list_filter = ('date', 'customer', 'status')
    date_hierarchy = 'date'
    ordering = ('-date',)
    search_fields = ["customer"]
    raw_id_fields = ('customer',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Quotation, QuotationAdmin)