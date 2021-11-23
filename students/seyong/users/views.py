import json, re

from django.http  import JsonResponse

from django.views import View
from users.models  import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name                 = data['name']
            email                = data['email']
            password             = data['password']
            phone_number         = data['phone_number']       
            self_introduction    = data['self_introduction']
            gender               = data['gender']

            email_regex          = "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            password_regex       = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"

            if not re.match(email_regex, email):
                return JsonResponse({"MESSAGE": "INVALID_EMAIL"}, status = 400)

            if not re.match(password_regex, password):
                return JsonResponse({"MESSAGE": "INVALID_PASSWORD"}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE": "EMAIL_ALREADY_EXISTS"}, status = 400)
            
            User.objects.create(
                name              = name,
                email             = email,
                password          = password,
                phone_number      = phone_number,
                self_introduction = self_introduction,
                gender            = gender
            )

            return JsonResponse({"MESSAGE": "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

class SignInView(View):
    def post(self, request):
        try:
            data                  = json.loads(request.body)

            email                 = data['email']
            password              = data['password']

            if not User.objects.filter(email = email).exists():
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status = 401)

            if not User.objects.get(email = email).password == password:
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status = 401)

            return JsonResponse({"MESSAGE": "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE" : "INVALID_USER"}, status=401)