import requests
import json

from django.shortcuts import render
from django.http import HttpResponse

from app.utils import data_extraction


def index(request):
    return render(request, 'app/index.html')


def send_message_to_telegram(request):
    try:
        secret_data = data_extraction()
        text = request.GET.get('text')
        callback = request.GET.get('callback')
        response = requests.get(
            f"https://api.telegram.org/bot{secret_data['BOT_TOKEN']}/"
            f"sendmessage?chat_id={secret_data['CHAT_ID']}&"
            f"text=business-card:     {text}",
        )
        key = 'response'

        print(response.status_code)
        if response.status_code == 200:
            data = json.dumps({key: 'сообщение отправлено'})
            return HttpResponse(f'{callback}({data})',
                                content_type='application/javascript')

        data = json.dumps({key: 'что-то пошло не так'})
        return HttpResponse(f'{callback}({data})',
                            content_type='application/javascript')

    except Exception as e:
        data = json.dumps({key: f'что-то пошло не так...\n{e}'})
        return HttpResponse(f'{callback}({data})',
                            content_type='application/javascript')
