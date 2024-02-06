# flake8:noqa
import os
from dotenv import load_dotenv

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def index(request):
    return render(request, 'app/index.html')


def share(request):
    url = {"url": f"https://api.telegram.org/bot{BOT_TOKEN}/sendmessage?"
                  f"chat_id={CHAT_ID}&text=business-card:     "}
    return JsonResponse(url)


def send_message_to_telegram(request, text):
    return HttpResponseRedirect(f"https://api.telegram.org/bot{BOT_TOKEN}/"
                                f"sendmessage?chat_id={CHAT_ID}&"
                                f"text=business-card:     {text}")
