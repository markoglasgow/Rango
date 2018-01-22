from django.contrib import admin
from rango.models import Category, Page

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'url']
    list_display = ('title', 'url')


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
