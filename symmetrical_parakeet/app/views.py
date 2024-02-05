# flake8:noqa
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'app/index.html')


def share(request):
    return JsonResponse({"url": """https://api.telegram.org/bot6216510134:AAFubMLITpcM02wVJu3WNvBKEvtN5KXxbT8/sendmessage?chat_id=-1001262768687&text=business-card:     """})
