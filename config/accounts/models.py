from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Telefon raqami")
    def __str__(self) -> str:
        return '%s %s (%s)'%(
            self.last_name,
            self.first_name,
            self.username,
        )
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = '1. Userlar'