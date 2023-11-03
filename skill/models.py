from django.db import models

# Create your models here.
class Language(models.Model):
    class Meta:
        verbose_name_plural = 'LANGUAGE'
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return self.name
    

class CoreSkill(models.Model):
    class Meta:
        verbose_name_plural = 'CORE SKILL'
    name = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return self.name
    

class OtherSkill(models.Model):
    class Meta:
        verbose_name_plural = 'OTHER SKILL'
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    


class CV(models.Model):
    class Meta:
        verbose_name_plural = 'RESUME LINK'
    cv_link = models.URLField()
    
    def __str__(self):
        return self.cv_link