from django.urls import path

from app.views import index, share


app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('share/', share, name='share'),
]
