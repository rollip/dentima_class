from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

import json


EMAIL_TARGET = 'rollip@yandex.ru'

def send_email(request):

    body = json.loads(request.body)
    name = body['name']
    email = body['email']
    phone = body['phone']
    page = body['page']
    subject = 'rollip@yandex.ru'
    message = f"Запись на семинар: \nСеминар: {page} \nИмя: {name}\nEmail: {email}\nТелефон: {phone}\n"
    from_email = 'rollip@yandex.ru'
    recipient_list = ['rollip@yandex.ru']

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently = False)
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("/seminar")
    else:
        return HttpResponse("Make sure all fields are entered and valid.")
