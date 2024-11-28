import requests
from random import choice
from datetime import datetime

from .models import *



def base_context(request):
    base_top5_articles = Article.objects.filter(published=True).order_by("-views")[:5]
    base_top5_random_article = choice(base_top5_articles)

    hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
    hafta_kuni = hafta_kunlari[datetime.now().weekday()]

    weather_data = requests.get('https://api.weatherapi.com/v1/current.json?q=Fergana&key=3eead9e64e5248bcbf8112613241811').json()
    temperature = {
        "temp_c": weather_data.get('current').get('temp_c'),
        "location": weather_data.get('location').get('name'),
        "icon": weather_data.get('current').get('condition').get('icon'),
    }
    context = {
        'base_top5_random_article': base_top5_random_article,
        'weekday': hafta_kuni,
        'today': str(datetime.today().strftime("%d-%m-%Y")).replace('-', '.'),
        'temperature': temperature,
    }
    return context