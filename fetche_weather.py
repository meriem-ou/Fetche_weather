import requests


class Weather:
    def __init__(self, api_key):
        self.city = api_key
    
    def weather(self):
        user_input = input("Enter Your City : ")
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={self.city}')

        if weather_data.status_code == 200:

            weather = weather_data.json()['weather'][0]['main']
            desc = weather_data.json()['weather'][0]['description']
            temp = weather_data.json()['main']['temp']
            humidity = weather_data.json()['main']['humidity']
            
            print(f'The weather in {user_input} is : {weather} that means : {desc}')
            print(f'The temprature is : {temp}°C')
            print(f'The weather is : {humidity}%') 

        else:
            if weather_data.status_code == 404:
                print('City not found.')
            else:
                print('Error fetching weather.')


data = Weather('28e98f672b2502726976e91bcc55c821')
print(data.weather())



