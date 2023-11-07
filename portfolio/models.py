from django.db import models
import uuid
from ckeditor.fields import RichTextField

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'CATEGORY'
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Portfolio(BaseModel):
    class Meta:
        verbose_name_plural = 'PORTFOLIO'
    category = models.ForeignKey(Category,related_name='category', on_delete=models.CASCADE)
    project_title = models.CharField(max_length=300)
    feature_image = models.ImageField(upload_to='images/portfolio/feature')
    RichTextField(null = True, blank = True)
    project_link = models.URLField()
    duration = models.CharField(max_length=30)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.project_title

class RelatedImage(BaseModel):
    class Meta:
        verbose_name_plural = 'RELATED IMAGE'
    project = models.ForeignKey(Portfolio,related_name='project', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/portfolio/related')

    def __str__(self):
        return str(self.uuid)