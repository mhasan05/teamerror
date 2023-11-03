from django.contrib import admin
from .models import *


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ['client_name','source','rating']
    
admin.site.register(Feedback,FeedbackAdmin)
