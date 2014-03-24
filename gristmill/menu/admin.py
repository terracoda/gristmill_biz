from django.contrib import admin
from menu.models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Menu, MenuAdmin)
