from django.db import models
# 이름, 이메일, 비밀번호, 연락처(휴대폰), 그 외 개인정보 
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=40, unique=True)
    introduce = models.CharField(max_length=150)
    gender = models.CharField(max_length=20, unique=True)
    class Meta:
        db_table = 'users'



created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

