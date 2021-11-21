import re, json

from django.db import IntegrityError
from django.http  import JsonResponse
from django.views import View

from .models import User 

class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            """
            KeyError 왜 나는거임?
            dictionary에서 KEY값을 넣어서 VALUE값을 가져오려고 할 때,
            KEY값을 불러올 수 없으면 에러
            """
            name           = data['name']
            email          = data['email']
            password       = data['password']
            phone_number   = data['phone_number'] 
            email_match    = re.compile('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')
            password_match = re.compile('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$')

            # if email == "" or password == "":
            #     return JsonResponse({"MESSAGE" : "aKEY_ERROR"}, status=400) 
            # if re.match(email_match, email) == None:

            if email_match.match(email) == None:
                return JsonResponse({"MESSAGE" : "EMAIL_ERROR"}, status=400)

            if re.match(password_match, password) == None:
                return JsonResponse({"MESSAGE" : "PASSWORD_ERROR"}, status=400)
            
            # email_list   = User.objects.values_list('email', flat=True)
            # if email in email_list:
            #     return JsonResponse({"중복된 이메일 존재합니다."}, status=400)                

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




















