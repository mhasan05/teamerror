from django.db import models
from portfolio.models import BaseModel
class Services(BaseModel):
    class Meta:
        verbose_name_plural = 'ALL SERVICE'
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    order_link = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Package(BaseModel):
    class Meta:
        verbose_name_plural = 'PACKAGE'
    package_name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    services = models.ManyToManyField(Services, blank=True)
    order_link = models.CharField(max_length=100)

    def __str__(self):
        return self.package_name