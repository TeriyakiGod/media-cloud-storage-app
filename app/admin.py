from django.contrib import admin

from .models import Media

admin.site.site_title = 'Cloud Media Storage'
admin.site.site_header = 'Cloud Media Storage'

admin.site.register(Media)