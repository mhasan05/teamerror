from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['category_name',]
    
admin.site.register(Category,CategoryAdmin)



class BlogsAdmin(admin.ModelAdmin):

    list_display = ['blog_title','blog_category','author']
    
admin.site.register(Blogs,BlogsAdmin)
