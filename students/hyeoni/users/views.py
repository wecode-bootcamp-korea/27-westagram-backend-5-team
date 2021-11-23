import re, json

from django.http  import JsonResponse
from django.views import View

from .models import User 

class SignUpView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)    
            user_name           = data['name']
            user_email          = data['email']
            user_password       = data['password']
            user_phone_number   = data['phone_number']

            if User.objects.filter(email=user_email).exists():
                return JsonResponse({"MESSAGE" : "중복된 이메일 존재합니다."}, status=400)   

            if not re.match('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', user_email):
                return JsonResponse({"MESSAGE" : "EMAIL_ERROR"}, status=400)

            if not re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$', user_password):
                return JsonResponse({"MESSAGE" : "PASSWORD_ERROR"}, status=400)

            User.objects.create(
                name         = user_name,
                email        = user_email,
                password     = user_password,
                phone_number = user_phone_number,
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data                = json.loads(request.body)
            user_email          = data['email']
            user_password       = data['password']

            if User.objects.get(email=user_email,password=user_password):
                return JsonResponse({"MESSAGE": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE" : "KEY_ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)