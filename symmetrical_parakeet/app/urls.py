from django.urls import path

from app.views import index, send_message_to_telegram


app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('send/', send_message_to_telegram),
]
