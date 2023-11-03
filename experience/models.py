from django.db import models

# Create your models here.
class Experience(models.Model):
    year_of_experience = models.CharField(max_length=10)
    completed_project = models.CharField(verbose_name='Order Complete',max_length=10)
    happy_customer = models.CharField(max_length=10)
    working_hour = models.CharField(max_length=10)

    def __str__(self):
        return self.year_of_experience