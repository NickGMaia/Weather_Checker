import requests
from dotenv import load_dotenv
import os
def get_weather_from_api(api_key, city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={api_key}&q={city}"

    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_weather(city_name):
    api_key = os.getenv("API_KEY")
    weather_data = get_weather_from_api(api_key, city_name)

    if weather_data and weather_data.get("cod") != "404":
        main_weather = weather_data["weather"][0]["main"]
        temperature = weather_data["main"]["temp"] - 273.15  # Convertendo de Kelvin para Celsius
        icon = weather_data["weather"][0]["icon"]

        return {
            "city_name": city_name,
            "main_weather": main_weather,
            "temperature": f"{temperature:.2f}",
            "icon": f"http://openweathermap.org/img/wn/{icon}.png"
        }
    return None

def get_periodo_dia():
    from datetime import datetime
    hora_atual = datetime.now().hour

    if 6 <= hora_atual < 12:
        return 'manha'
    elif 12 <= hora_atual < 18:
        return 'tarde'
    else:
        return 'manha'
