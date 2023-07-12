from django.db import models
from accounts.models import User
from django.utils import timezone
from datetime import timedelta

UZBEK = "O'zbek"
RUS = "Rus"
LANGUAGE_CHOICES = (
    (UZBEK, UZBEK),
    (RUS, RUS),
)


class ConcertPost(models.Model):
    title = models.CharField(max_length=200, null=True, verbose_name="Konsert nomi")
    image = models.ImageField(upload_to='images/post', verbose_name='Rasm')
    date = models.DateField(auto_now_add=False, verbose_name="Konsert sanasi")

    language  = models.CharField(max_length=10, verbose_name="Post chiqariladigan til", choices=LANGUAGE_CHOICES, default=UZBEK)

    def __str__(self) -> str:
        return self.title
    
    @property
    def holati(self):
        now = timezone.now() + timedelta(hours=5)
        max_date = self.date
        if now.date() > max_date:
            return "Tugagan"
        else:
            return "Tugamagan" 
    class Meta:
        verbose_name = 'Konsert '
        verbose_name_plural = '1. Konsertlar'


class Event(models.Model):
    image = models.ImageField(upload_to='images/events', verbose_name="Rasm")
    date = models.DateField(auto_now_add=False, verbose_name="Sana")
    description = models.TextField(null=True, verbose_name="Qisqa ma'lumot")
    title = models.CharField(max_length=300, verbose_name="Nomi")

    language  = models.CharField(max_length=10, verbose_name="Post chiqariladigan til", choices=LANGUAGE_CHOICES, default=UZBEK)

    @property
    def holati(self):
        now = timezone.now() + timedelta(hours=5)
        max_date = self.date
        if now.date() > max_date:
            return "Tugagan"
        else:
            return "Tugamagan" 

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Tadbir '
        verbose_name_plural = '2. Tadbirlar'