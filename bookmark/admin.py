from django.contrib import admin
from .models import Bookmark

# Register your models here.



class BookmarkOptions(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'url', 'contents']
    # list_editable = ['site_name', 'url']
    list_filter = ['url']
    search_fields = ['site_name', 'url', 'contents']



admin.site.register(Bookmark, BookmarkOptions)