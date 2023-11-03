from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from account.manager import UserManager #import from uauth apps


class UserAccount(AbstractBaseUser,PermissionsMixin):
    class Meta:
        verbose_name_plural = "USER"
    profile_pic = models.ImageField(upload_to='faces/', default='faces/profile.png')
    username = models.CharField(max_length=15,unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    designation = models.CharField(default='Back-end Developer',max_length=100)
    email = models.EmailField(max_length=100)
    phone_home = models.CharField(max_length=14)
    phone_office = models.CharField(max_length=14)
    auth_token = models.CharField(max_length=500,null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name','email','phone_home','phone_office']

    objects = UserManager()

    def __str__(self):
        return self.username