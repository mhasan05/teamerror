from django.contrib import admin
from .models import *


class LanguageAdmin(admin.ModelAdmin):

    list_display = ['name',]
    
admin.site.register(Language,LanguageAdmin)


class CoreSkillAdmin(admin.ModelAdmin):

    list_display = ['name',]
    
admin.site.register(CoreSkill,CoreSkillAdmin)



class OtherSkillAdmin(admin.ModelAdmin):

    list_display = ['name',]
    
admin.site.register(OtherSkill,OtherSkillAdmin)



class CVAdmin(admin.ModelAdmin):

    list_display = ['cv_link',]
    
admin.site.register(CV,CVAdmin)