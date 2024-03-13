from django.contrib import admin
from django.utils.safestring import mark_safe
from ilanlar.models import Brands,Ilanlar

# Register your models here.

class AdminMarkalar(admin.ModelAdmin):
    list_display = ('ResimGoster','title', )
    prepopulated_fields = {'slug': ('title',)}

    def ResimGoster(self, obj):
        return mark_safe('<img src="{}" width="25" height="25"/>'.format(obj.image.url))


admin.site.register(Brands, AdminMarkalar)


class Adminilanlar(admin.ModelAdmin):
    list_display = ('ResimGoster','title','brand','price','slug','create_time','goruntulenme_sayisi')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ["brand","status", "create_time",]
    
    def ResimGoster(self, obj):
        return mark_safe('<img src="{}" height="75" width="100"/>'.format(obj.banner.url))

admin.site.register(Ilanlar,Adminilanlar)