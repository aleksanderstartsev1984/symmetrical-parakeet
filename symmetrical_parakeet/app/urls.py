from django.urls import path

from app.views import index, share, send_message_to_telegram


app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('share/', share, name='share'),
    path('send/<str:text>/', send_message_to_telegram, name='send'),
]
