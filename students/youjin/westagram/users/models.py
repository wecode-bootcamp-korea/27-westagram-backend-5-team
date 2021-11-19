from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=200, unique=True, blank=True, null=True)
    passward     = models.CharField(max_length=100)
    phone_number = models.PhoneNumberField(unique=True)
    gender       = models.CharField(max_length=50)
    sns          = models.BooleanField()
    create_date  = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True) 

    class Meta:
        db_table = 'users'
