from django.contrib import admin

from daily_grist.models import Entry

class EntryAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title', 'id', 'pub_date','enable_comments', 'status')
	search_fields = ['title', 'body_markdown']
	list_filter = ('pub_date', 'enable_comments', 'status')
	prepopulated_fields = {"slug": ('title',)}
	
	fieldsets = (
        (None, {'fields': (('title', 'status'), 'lead_image', 'body_markdown', ('pub_date', 'enable_comments'),'tags', 'slug')}),
    )

admin.site.register(Entry, EntryAdmin)