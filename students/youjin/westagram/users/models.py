from django.db import models
from django.db.models.fields import BooleanField
# from django.db.models.fields import BooleanField

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=200, unique=True, blank=True, null=True)
    passward     = models.CharField(max_length=100)
    phone_number = models.PhoneNumberField(unique=True)
    gender       = models.CharField(max_length=50)
    sns          = models.BooleanField()

    class Meta:
        db_table = 'users'
