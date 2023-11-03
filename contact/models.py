from django.db import models

class Support(models.Model):
    class Meta:
        verbose_name_plural = 'SUPPORT MESSAGE'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    

class Social(models.Model):
    class Meta:
        verbose_name_plural = 'SOCIAL USERNAME'
    linkedin = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)

    def __str__(self):
        return self.linkedin
    


class Address(models.Model):
    class Meta:
        verbose_name_plural = 'ADDRESS'
    address = models.TextField(default='Soguna,Belkuchi',max_length=200)
    city = models.CharField(default='Sirajganj',max_length=100)
    country = models.CharField(default='Bangladesh',max_length=100)

    def __str__(self):
        return self.address

