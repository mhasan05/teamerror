from django.urls import path
from .views import BlogsView,SingleBlog
urlpatterns = [
    path('',BlogsView.as_view(),name='blogs' ),
    path('post/<str:uuid>',SingleBlog.as_view(),name='blog_post' ),
]