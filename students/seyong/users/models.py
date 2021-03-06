from django.db import models

class User(models.Model):
    name              = models.CharField(max_length=20)
    email             = models.CharField(max_length=45, unique=True)
    password          = models.CharField(max_length=200)
    phone_number      = models.CharField(max_length=40, unique=True)
    self_introduction = models.CharField(max_length=150)
    gender            = models.CharField(max_length=20)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'




