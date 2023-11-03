from django.db import models
from portfolio.models import BaseModel
from account.models import UserAccount
from ckeditor.fields import RichTextField

class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'CATEGORY'
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return (self.category_name)


class Blogs(BaseModel):
    class Meta:
        verbose_name_plural = 'BLOGS'
    blog_title = models.CharField(max_length=200)
    feature_image = models.ImageField(upload_to='images/blogs/')
    description = RichTextField(null = True, blank = True)
    blog_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title
