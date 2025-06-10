import requests

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f'Weather in {city}')
        print(f'Temperature: {data["main"]["temp"]} C')
        print(f'Humidity: {data["main"]["humidity"]} %')
    else:
        print('Failed error')

api_key = 'api_key'
get_weather('Tashkent', api_key)