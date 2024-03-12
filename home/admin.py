from django.contrib import admin
from django.utils.safestring import mark_safe
from home.models import Settings

# Register your models here.

class SettCustom(admin.ModelAdmin):
    list_display = ('display_image','title', )

    def display_image(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    display_image.short_description = 'Image'

admin.site.register(Settings)
