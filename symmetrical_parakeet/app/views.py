# flake8:noqa
from pprint import pprint

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect


def index(request):
    return render(request, 'app/index.html')


def share(request):
    res = str(request.headers)

    print('##################################################################')
    pprint(str(res))
    print('##################################################################')

    url = {"url": "https://api.telegram.org/bot6216510134:AAFubMLITpcM02wVJu3WNvBKEvtN5KXxbT8/sendmessage?chat_id=-1001262768687&text=business-card:     "}
    url['response'] = str(res)
    return JsonResponse(url)


def send_message_to_telegram(request, text):
    return HttpResponseRedirect(f"https://api.telegram.org/bot6216510134:AAFubMLITpcM02wVJu3WNvBKEvtN5KXxbT8/sendmessage?chat_id=-1001262768687&text=business-card:     {text}")
