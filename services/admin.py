from django.contrib import admin
from .models import *


class ServicesAdmin(admin.ModelAdmin):

    list_display = ['title',]
    
admin.site.register(Services,ServicesAdmin)


class PackageAdmin(admin.ModelAdmin):

    list_display = ['package_name',]
    
admin.site.register(Package,PackageAdmin)