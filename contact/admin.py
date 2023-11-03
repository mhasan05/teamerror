from django.contrib import admin
from .models import *


class SupportAdmin(admin.ModelAdmin):

    list_display = ['name','email','message']
    
admin.site.register(Support,SupportAdmin)


class SocialAdmin(admin.ModelAdmin):

    list_display = ['linkedin','github','facebook']
    
admin.site.register(Social,SocialAdmin)


class AddressAdmin(admin.ModelAdmin):

    list_display = ['address','city','country']
    
admin.site.register(Address,AddressAdmin)
