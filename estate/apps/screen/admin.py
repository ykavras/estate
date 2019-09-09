from django.contrib import admin

from .models import *


class HotSpotAdmin(admin.ModelAdmin):
    list_display = ('text', 'screen')
    list_filter = ('screen', )

admin.site.register(Screen)
admin.site.register(HotSpot, HotSpotAdmin)