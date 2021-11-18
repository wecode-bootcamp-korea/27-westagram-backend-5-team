from django.db import models
# from django.db.models.fields import BooleanField

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.CharField(max_length=50)
    passward     = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    gender       = models.CharField(max_length=50)
    sns          = models.BooleanField()

    class Meta:
        db_table = 'users'
