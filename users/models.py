from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    name = models.CharField(max_length=50, verbose_name="Ім'я")
    surname = models.CharField(max_length=50, verbose_name="Призвіще")
    email = models.EmailField(max_length=254, verbose_name="email")
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Телефон")
    
    
    def __str__(self):
        return self.name + " " + self.surname