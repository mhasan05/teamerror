from django.contrib import admin
from .models import *


class ExperienceAdmin(admin.ModelAdmin):

    list_display = ['year_of_experience','completed_project','happy_customer','working_hour']
    
admin.site.register(Experience,ExperienceAdmin)