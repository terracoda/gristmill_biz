from django.contrib import admin
from homepage.models import PageIntro, TeaserImage, Teaser

class PageIntroAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'pub_date',)
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    search_fields = ["title"]
 
    fieldsets = (
        (None, {'fields': (('title', 'status'), 'intro_text_markdown',)}),
    )

class TeaserImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'name','description', 'pub_date',)
	list_filter = ('pub_date',)
	date_hierarchy = 'pub_date'
	search_fields = ["title", "name", "description"]

class TeaserAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date','link_url',)
	list_filter = ('pub_date',)
	date_hierarchy = 'pub_date'
	ordering = ('order',)
	search_fields = ["title", "link_url"]

admin.site.register(PageIntro, PageIntroAdmin)
admin.site.register(TeaserImage, TeaserImageAdmin)
admin.site.register(Teaser, TeaserAdmin)