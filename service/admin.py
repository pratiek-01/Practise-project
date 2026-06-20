from django.contrib import admin
from service.models import Service
from service.models import About

class serviceAdmin(admin.ModelAdmin):
    list_display=('ser_title','ser_data')

admin.site.register(Service,serviceAdmin)


class abAdmin(admin.ModelAdmin):
    list_display=('ab_title','ab_data')

admin.site.register(About,abAdmin)
# Register your models here.
