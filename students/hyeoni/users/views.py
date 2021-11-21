import re, json

from django.db import IntegrityError
from django.http  import JsonResponse
from django.views import View

from .models import User 

class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)    
            name           = data['name']
            email          = data['email']
            password       = data['password']
            phone_number   = data['phone_number'] 
            email_match    = re.compile('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')
            password_match = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$')
            if email_match.match(email) == None:
                return JsonResponse({"MESSAGE" : "EMAIL_ERROR"}, status=400)
            if password_match.match(password) == None:
                return JsonResponse({"MESSAGE" : "PASSWORD_ERROR"}, status=400)          
            User.objects.create(
                name         = name,
                email        = email,
                password     = password,
                phone_number = phone_number,
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)
        except IntegrityError:
            return JsonResponse({"MESSAGE" : "IntegrityError"}, status=400)




















