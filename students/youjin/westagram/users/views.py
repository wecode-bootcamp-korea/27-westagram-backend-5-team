from django.http  import JsonResponse
from django.views import View

from .models import User

import json
import re

class UserView(View):
    def post(self, request):
        # users_email    = re.compile()
        # users_password = re.compile()
        data              = json.loads(request.body)
        user_name         = data['name']
        user_email        = data['email']
        user_password     = data['password']
        user_phone_number = data['phone_number']
        user_gender       = data['gender']
        user_sns          = data['sns']

        try:
            if re.match('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', user_email) is None :  
                return JsonResponse({"message": "KEY_ERROR"}, status=400)
            
            if User.objects.filter(email=user_email).exists():
                return JsonResponse({"message" : "이미 존재하는 이메일입니다. 이메일을 다시 입력해주세요."}, status=400)
            
            if re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$', user_password) is None:
                return JsonResponse({"message": "KEY_ERROR"}, status=400)

            users = User.objects.create(
                name         = user_name,    
                email        = user_email,
                password     = user_password,
                phone_number = user_phone_number,
                gender       = user_gender,
                sns          = user_sns,
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except:
            return JsonResponse({"message": "ERROR"}, status=404)
