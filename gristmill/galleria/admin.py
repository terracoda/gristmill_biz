from django.contrib import admin
from galleria.models import Tag, Image

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ImageAdmin(admin.ModelAdmin):
	list_display = ('caption', 'id', 'filename', 'pub_date',)
	list_filter = ('pub_date', 'tags',)
	date_hierarchy = 'pub_date'
	ordering = ('-pub_date',)
	filter_horizontal = ('tags',)
	search_fields = ["caption"]

admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
