from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['category_name',]
admin.site.register(Category,CategoryAdmin)

class RelatedImageAdmin(admin.StackedInline):
    model = RelatedImage

    list_display = ['project',]

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [RelatedImageAdmin]
    list_display = ['project_title','category']
    
admin.site.register(Portfolio,PortfolioAdmin)




