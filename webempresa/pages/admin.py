from django.contrib import admin

# Register your models here.
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')


admin.site.register(Page, PageAdmin)
