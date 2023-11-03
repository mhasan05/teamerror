from django.db import models
from portfolio.models import BaseModel

class Feedback(BaseModel):
    class Meta:
        verbose_name_plural = 'FEEDBACK'
    client_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/feedback/client')
    source = models.CharField(max_length=50)
    review = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.client_name
