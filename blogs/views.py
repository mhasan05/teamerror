from django.shortcuts import render
from django.views import View
from .models import Blogs


class BlogsView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blogs.objects.all()
        active_page = "Blogs"
        data = {'blogs':blogs,'active_page':active_page}
        return render(request,'blogs.html',context=data)

class SingleBlog(View):    
    def get(self, request, uuid):
        blog = Blogs.objects.get(uuid = uuid)
        all_blogs = Blogs.objects.all()
        active_page = "Blogs"
        data = {'blog':blog,'all_blogs':all_blogs,'active_page':active_page}
        return render(request,'blog-post.html',context=data)