import json, re

from django.http  import JsonResponse
from django.views import View

from .models import User

class UserView(View):
    def post(self, request):
        try:
            data              = json.loads(request.body)
            user_name         = data['name']
            user_email        = data['email']
            user_password     = data['password']
            user_phone_number = data['phone_number']
            user_gender       = data['gender']
            user_sns          = data['sns']

            if not re.match('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', user_email):  
                return JsonResponse({"message": "EMAIL_ERROR"}, status=400)
            
            if User.objects.filter(email=user_email).exists():
                return JsonResponse({"message" : "email_alreay_exists"}, status=400)
            
            if not re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$', user_password):
                return JsonResponse({"message": "PASSWORD_ERROR"}, status=400)

            User.objects.create(
                name         = user_name,    
                email        = user_email,
                password     = user_password,
                phone_number = user_phone_number,
                gender       = user_gender,
                sns          = user_sns
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def POST(self, request):
        try:
            data           = json.load(request.body)
            user_email     = data['email']
            user_password  = data['password']
            
            if not User.objects.filter(email = user_email, password = user_password).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401)        

            return JsonResponse({"message": "SUCCESS"}, status=200)
            
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)