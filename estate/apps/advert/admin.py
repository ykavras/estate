from django.contrib import admin

from .models import *


class AdvertImageInline(admin.TabularInline):
    model = AdvertImage


class AdvertAdmin(admin.ModelAdmin):
    inlines = (AdvertImageInline,)


admin.site.register(Advert, AdvertAdmin)
admin.site.register(HeatType)
admin.site.register(Project)
admin.site.register(Property)
admin.site.register(PropertyTitle)
admin.site.register(Room)
admin.site.register(Type)
