from django.conf import settings


def data_extraction() -> dict:
    """Извлекает данные из фафйла .env"""
    with open(f'{settings.BASE_DIR}/.env') as f:
        data = f.readlines()
        data = [i.rstrip('\n') for i in data]
        data = dict(i.split('=') for i in data)
        return data
