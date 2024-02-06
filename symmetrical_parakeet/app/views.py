# flake8:noqa
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect


def data_extraction():
    with open(f'{settings.BASE_DIR}/.env') as f:
        data = f.readlines()
        data = [i.rstrip('\n') for i in data]
        data = dict(i.split('=') for i in data)
        return data


def index(request):
    return render(request, 'app/index.html')


def share(request):
    secret_data = data_extraction()
    url = {"url": f"https://api.telegram.org/bot{secret_data['BOT_TOKEN']}/"
                  f"sendmessage?chat_id={secret_data['CHAT_ID']}&"
                  "text=business-card:     "}
    return JsonResponse(url)


def send_message_to_telegram(request, text):
    secret_data = data_extraction()
    return HttpResponseRedirect(
        f"https://api.telegram.org/bot{secret_data['BOT_TOKEN']}/sendmessage?"
        f"chat_id={secret_data['CHAT_ID']}&text=business-card:     {text}"
    )
